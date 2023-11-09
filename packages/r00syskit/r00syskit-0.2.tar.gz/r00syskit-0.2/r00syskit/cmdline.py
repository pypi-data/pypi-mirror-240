import os
import shlex
import subprocess

from r00log.logger import log
from r00timekit.elapsed import Elapsed
from . import CMD
from .platforms import platforms


class CmdOptions:
    shell_operators = ["|", ">", "<", "&"]
    shell_commands = ['alias',
                      'cd',
                      'cls',
                      'copy',
                      'del',
                      'dir',
                      'echo',
                      'exit',
                      'mkdir',
                      'touch',
                      'export',
                      'history',
                      'move',
                      'set',
                      'source',
                      'type',
                      'unset']
    shell_extensions = ['.bat', '.sh', '.ps1']

    def __init__(self, command: str | list, timeout=CMD.WAIT):
        self.__input_comand = command
        self._command_str: str = ''
        self._command_list: str = ''
        self.command: str | list = ''
        self.timeout: int = timeout
        self.shell: bool = False
        self.encoding: str = CMD.ENCODING

    @staticmethod
    def _is_redirection_operators(command_str: str) -> bool:
        # Если присутстуют операторы перенаправления
        for op in CmdOptions.shell_operators:
            if op in command_str:
                return True
        return False

    @staticmethod
    def _is_shell_commands(command_str: str) -> bool:
        # Если это программы связанные с оболочкой (source, export, alias, copy, move...)
        for program in CmdOptions.shell_commands:
            if program in command_str:
                return True
        return False

    @staticmethod
    def _is_run_scripts(command_str: str) -> bool:
        # Если команда запускает скрипты
        for ext in CmdOptions.shell_extensions:
            if ext in command_str:
                return True
        return False

    def _detect_shell(self):
        return (self._is_redirection_operators(self._command_str) or
                # self._is_shell_commands(self._command_list) or
                self._is_run_scripts(self._command_str) or
                '\\' in self._command_str)

    def reformat(self):
        if isinstance(self.__input_comand, str):
            self._command_str = self.__input_comand
            self._command_list = shlex.split(self._command_str, posix=os.name != 'nt')
        else:
            self._command_list = self.__input_comand
            self._command_str = ' '.join(self._command_list)

        self.shell = self._detect_shell()

        if platforms.is_linux or 'shell' in self._command_str:
            self.command = self._command_str
            self.encoding = CMD.ENCODING
        else:
            self.command = self._command_str if self.shell else self._command_list
            self.encoding = 'cp866'
        return self


class CmdResult(str):
    def __new__(cls, output, status):
        obj = str.__new__(cls, output)
        obj.status = status
        return obj

    @property
    def is_success(self):
        return self.status == 0

    def strip(self, chars=None):
        stripped_output = super().strip(chars)
        return CmdResult(stripped_output, self.status)


# noinspection PyProtectedMember
class CmdRun:
    def __call__(self, command: str, timeout: int = CMD.WAIT) -> CmdResult:
        options = CmdOptions(command, timeout).reformat()
        result = self._run_command(options)
        return result.strip()

    @staticmethod
    def force(command) -> None:
        options = CmdOptions(command).reformat()
        with open(os.devnull, 'w') as fp:
            subprocess.Popen(options.command, shell=options.shell, stdout=fp, stderr=fp, encoding=options.encoding)

    def _run_command(self, options: CmdOptions) -> CmdResult:
        elapsed = Elapsed()
        elapsed.start()

        try:
            result = subprocess.run(options.command,
                                    stdout=subprocess.PIPE,
                                    timeout=options.timeout,
                                    stderr=subprocess.STDOUT,
                                    shell=options.shell,
                                    encoding=options.encoding,
                                    text=True)
            stdout = result.stdout
            if not stdout and result.returncode == 0:
                stdout = 'success'
            self._log(elapsed.result, options._command_str, options.shell, result.returncode, stdout)
            return CmdResult(stdout, result.returncode)
        except FileNotFoundError:
            msg = f'Invalid command: {options._command_str}'
        except subprocess.TimeoutExpired:
            msg = f'Command timeout [{options.timeout} sec]: {options._command_str}'
        except Exception as e:
            msg = f'Unknown error: {e}'

        self._log(elapsed.result, options._command_str, options.shell, -1)
        return CmdResult(msg, 1)

    @staticmethod
    def _log(elpsed, command_str, shell, returncode, stdout=None):
        trace = getattr(log, 'trace')
        warn = getattr(log, 'warning')
        stdout = stdout.strip() + ', ' if stdout else ''
        stdout = '\n' + stdout if '\n' in stdout else stdout
        msg = f'{elpsed} {command_str} ⇝ {stdout}shell: {shell}, code: {returncode}'
        trace(msg) if returncode == 0 else warn(msg)


cmd = CmdRun()

if __name__ == '__main__':
    cmd('adb devices')
    cmd('adb shell ls -la')
    cmd('adb shell su -c find "/sys/devices/" -name "brightness"')
    cmd('adb shell "su -c \'echo 10 > /data/local/tmp/211.txt\'"')
    cmd('adb shell su -c id')
    cmd('adb shell "echo 10 > /data/local/tmp/3.txt"')
    cmd('adb shell cat /data/local/tmp/2.txt')
    cmd('echo Hello, World!')
    cmd('invalid_command')
    cmd('echo Привет, Мир!')
    cmd('adb shell ls')
    cmd('adb invalid_command')
    cmd.force(r'mkdir c:\temp\FORCE')
    cmd(r'mkdir c:\temp\FORCE')
    cmd(r'del /S /Q c:\temp\FORCE')
    cmd('echo Hello | find "Hello"')
    cmd('echo Hello | grep "Hello"')
    cmd('type temp.txt')
    cmd('del temp.txt')
    cmd('ping 127.0.0.1 -n 3', timeout=4)
    cmd('ping 127.0.0.1 -n 1', timeout=5)
    cmd('ping 127.0.0.1 -n 5', timeout=1)
    cmd('adb shell echo Привет, Мир!')
    cmd('ipconfig')
    cmd('tasklist')
    cmd('set')
    cmd('adb shell invalid_command')

    cmd('echo Hello > files.txt')
    cmd('adb push files.txt /sdcard/')
    cmd('adb pull /sdcard/files.txt')
    cmd('adb shell rm /sdcard/files.txt')

    cmd('adb shell pm list packages')
    cmd('adb shell dumpsys')
    cmd('adb shell dumpsys battery')
    cmd('echo first && echo second')
    cmd('echo first & echo second')
    cmd('echo Hello, World! | findstr Hello')
    cmd('batch_file.bat')
    cmd('powershell -FileUtil script.ps1')
    cmd('net user')
    cmd('adb shell sh /sdcard/script.sh')
    cmd('echo DONE !')
