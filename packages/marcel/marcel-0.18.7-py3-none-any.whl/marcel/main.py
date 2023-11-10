# This file is part of Marcel.
# 
# Marcel is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or at your
# option) any later version.
# 
# Marcel is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Marcel.  If not, see <https://www.gnu.org/licenses/>.

# This file is part of Marcel.
#
# Marcel is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or at your
# option) any later version.
#
# Marcel is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with Marcel.  If not, see <https://www.gnu.org/licenses/>.

import atexit
import multiprocessing
import os
import pathlib
import readline
import sys
import time

import marcel.builtin
import marcel.core
import marcel.env
import marcel.exception
import marcel.job
import marcel.locations
import marcel.multilinereader
import marcel.opmodule
import marcel.parser
import marcel.reservoir
import marcel.tabcompleter
import marcel.util

HISTORY_LENGTH = 1000


class Reader(marcel.multilinereader.MultiLineReader):

    def __init__(self, env, history_file):
        super().__init__(history_file=history_file)
        self.env = env

    def take_edited_command(self):
        edited_command = self.env.edited_command
        self.env.edited_command = None
        return edited_command


class ReloadConfigException(BaseException):

    def __init__(self):
        super().__init__()


class SameProcessMode:

    def __init__(self, main, same_process):
        self.main = main
        self.original_same_process = main.same_process
        self.new_same_process = same_process

    def __enter__(self):
        self.main.same_process = self.new_same_process

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.main.same_process = self.original_same_process


class Main:

    def __init__(self, config_file, same_process, old_namespace):
        # sys.argv sets config_path, dill
        self.dill = True
        self.main_pid = os.getpid()
        #
        self.same_process = same_process
        try:
            self.env = marcel.env.Environment.new(config_file, old_namespace)
        except marcel.exception.KillCommandException as e:
            print(f'Cannot start marcel: {e}', file=sys.stderr)
            sys.exit(1)
        except marcel.exception.KillShellException as e:
            print(f'Cannot start marcel: {e}', file=sys.stderr)
            sys.exit(1)
        self.tab_completer = marcel.tabcompleter.TabCompleter(self)
        self.op_modules = marcel.opmodule.import_op_modules(self.env)  # op name -> OpModule
        self.env.op_modules = self.op_modules
        self.reader = None
        self.initialize_reader()  # Sets self.reader
        self.input = None
        self.env.reader = self.reader
        self.job_control = marcel.job.JobControl.start(self.env, self.update_namespace)
        self.config_time = time.time()
        self.run_startup()
        self.run_script(marcel.builtin._COMMANDS)
        atexit.register(self.shutdown)

    def __getstate__(self):
        assert False

    def __setstate__(self, state):
        assert False

    def run(self, print_prompt):
        try:
            while True:
                try:
                    if self.input is None:
                        prompts = self.env.prompts() if print_prompt else (None, None)
                        self.input = self.reader.input(*prompts)
                    # else: Restarted main, and self.line was from the previous incarnation.
                    self.check_for_config_update()
                    self.run_command(self.input)
                    self.input = None
                    self.job_control.wait_for_idle_foreground()
                except KeyboardInterrupt:  # ctrl-C
                    print()
        except EOFError:  # ctrl-D
            print()

    def run_command(self, line):
        if line:
            try:
                parser = marcel.parser.Parser(line, self)
                pipeline = parser.parse()
                pipeline.set_error_handler(Main.default_error_handler)
                # self.run_immediate(pipeline) depends on whether the pipeline has a single op.
                # So check this before tacking on the out op.
                run_immediate = self.run_immediate(pipeline)
                # Append an out op at the end of pipeline, if there is no output op there already.
                if not pipeline.last_op().op_name() == 'write':
                    pipeline.append(marcel.opmodule.create_op(self.env, 'write'))
                command = marcel.core.Command(line, pipeline)
                if run_immediate:
                    command.execute(self.env)
                else:
                    self.job_control.create_job(command)
            except marcel.parser.EmptyCommand:
                pass
            except marcel.exception.KillCommandException as e:
                marcel.util.print_to_stderr(e, self.env)
            except marcel.exception.KillAndResumeException:
                # Error handler printed the error
                pass

    def run_api(self, pipeline):
        command = marcel.core.Command(None, pipeline)
        try:
            command.execute(self.env)
        except marcel.exception.KillCommandException as e:
            marcel.util.print_to_stderr(e, self.env)

    def initialize_reader(self):
        readline.set_history_length(HISTORY_LENGTH)
        readline.parse_and_bind('tab: complete')
        readline.parse_and_bind('set editing-mode emacs')
        readline.parse_and_bind('set completion-query-items 50')
        readline.set_pre_input_hook(self.insert_edited_command)
        self.reader = Reader(self.env, self.env.locations.history_path())

    def shutdown(self, restart=False):
        namespace = self.env.namespace
        self.job_control.shutdown()
        self.reader.close()
        if not restart:
            marcel.reservoir.shutdown(self.main_pid)
        return namespace

    def insert_edited_command(self):
        command = self.reader.take_edited_command()
        if command:
            readline.insert_text(command)
            readline.redisplay()

    def update_namespace(self, child_namespace_changes):
        # pwd requires special handling
        try:
            pwd = child_namespace_changes['PWD']
            self.env.dir_state().cd(pathlib.Path(pwd))
        except KeyError:
            # PWD wasn't changed
            pass
        self.env.namespace.update(child_namespace_changes)

    def run_startup(self):
        run_on_startup = self.env.getvar('RUN_ON_STARTUP')
        if run_on_startup:
            if type(run_on_startup) is str:
                self.run_script(run_on_startup)
            else:
                fail(f'RUN_ON_STARTUP must be a string')

    def run_script(self, script):
        with SameProcessMode(self, True):
            command = ''
            for line in script.split('\n'):
                if len(line.strip()) > 0:
                    if line.endswith('\\'):
                        command += line[:-1]
                    else:
                        command += line
                        self.run_command(command)
                        command = ''
            if len(command) > 0:
                self.run_command(command)

    def check_for_config_update(self):
        config_path = self.env.config_path
        config_mtime = config_path.stat().st_mtime if config_path.exists() else 0
        if config_mtime > self.config_time:
            raise ReloadConfigException()

    @staticmethod
    def default_error_handler(env, error):
        print(error.render_full(env.color_scheme()), flush=True)

    def run_immediate(self, pipeline):
        return (
                # For the execution of tests and scripts
                self.same_process or
                pipeline.first_op().run_in_main_process() or
                # This takes care of # side effects we want to keep,
                # e.g. (INTERACTIVE_EXECUTABLES.append(...))
                pipeline.first_op().op_name() == 'map')


def fail(message):
    print(message, file=sys.stderr)
    exit(1)


# --dill: bool
# --mpstart: fork/spawn/forkserver. Use fork if not specified
def args():
    flags = ('--dill', '--mpstart')
    dill = True
    mpstart = 'fork'
    script = None
    flag = None
    for arg in sys.argv[1:]:
        if arg in flags:
            flag = arg
            # For a boolean flag, set to True. A different value may be specified by a later arg.
            if flag == '--dill':
                dill = True
        elif arg.startswith('-'):
            fail(f'Unrecognized flag {arg}')
        else:
            if flag is None:
                # arg must be a script name
                script = arg
            else:
                # arg is a flag value
                if flag == '--dill':
                    dill = arg.lower() in ('t', 'true')
                elif flag == '--mpstart':
                    if arg in ('fork', 'spawn', 'forkserver'):
                        mpstart = arg
                    else:
                        fail(f'Set --mpstart to fork (default), forkserver, or spawn')
                flag = None
    return dill, mpstart, script


def main():
    dill, mpstart, script = args()
    old_namespace = None
    input = None
    if mpstart is not None:
        multiprocessing.set_start_method(mpstart)
    while True:
        MAIN = Main(None, same_process=False, old_namespace=old_namespace)
        MAIN.input = input
        MAIN.dill = dill
        print_prompt = sys.stdin.isatty()
        if script is None:
            # Interactive
            try:
                MAIN.run(print_prompt)
                break
            except ReloadConfigException:
                input = MAIN.input
                old_namespace = MAIN.shutdown(restart=True)
                pass
        else:
            # Script
            try:
                with open(script, 'r') as script_file:
                    MAIN.run_script(script_file.read())
            except FileNotFoundError:
                fail(f'File not found: {script}')
            break


if __name__ == '__main__':
    main()
