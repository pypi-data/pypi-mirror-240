from platform import system
import os

class Platforms:
    @property
    def is_windows(self):
        return system() == 'Windows'

    @property
    def is_linux(self):
        return system() == 'Linux'

    @property
    def is_pycharm(self):
        return True if 'PYCHARM_HOSTED' in os.environ else False

    @staticmethod
    def get_os_type():
        return system()


platforms = Platforms()

if __name__ == '__main__':
    print(platforms.is_windows)
    print(platforms.is_linux)
    print(platforms.is_pycharm)