import sys

from r00log.logger import log
from .cmdline import cmd


def kill_process(name: str) -> bool:
    """
    Убиваем запущенный процесс на Windows или Linux.
    :param name: Имя процесса. Расширение можно опустить.
    :return: bool
    """
    if sys.platform.startswith('win'):
        import psutil
        name += ".exe" if not name.endswith(".exe") else ""
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == name:
                log.info(f"Process found: {name}. Killed!")
                proc.kill()
                return True
        return False
    else:
        try:
            result = cmd(f'pkill {name}')
            if result.is_success:
                log.info(f"Process {name} killed successfully.")
                return True
        except:
            pass
        return False
