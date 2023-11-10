import time

from r00log.logger import log


class Elapsed:
    """
    Замеряет время между блоками
    Использование:
    elapsed.start()
    time.sleep(1)
    elapsed.print('Elapsed:')

    elapsed.start()
    time.sleep(1)
    print(elapsed.result)
    """

    def __init__(self):
        self._t0 = None

    def start(self):
        self._t0 = time.time()

    @staticmethod
    def __format(value: float) -> str:
        return f'[{round(value, 1)} sec]' if value else 'elapsed not start()'

    def __get_result(self):
        if self._t0:
            result = time.time() - self._t0
            self._t0 = None
            return result

    @property
    def current(self):
        return time.time() - self._t0 if self._t0 else -1

    @property
    def result(self) -> str:
        return self.__format(self.__get_result())

    def print(self, text='Elapsed time:') -> None:
        log.debug(f'{text} {self.result}')
