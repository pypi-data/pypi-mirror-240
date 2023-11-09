import time
from functools import wraps

from r00log.logger import log


def timeit(func):
    """Выводит в лог, время выполнения функции"""

    @wraps(func)
    def magic(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = round(time.time() - start, 3)
        log.debug(f"{func.__name__} elapsed: {elapsed} sec")
        return result

    return magic


class TimeBound:
    """
    Замена этого блока кода:
    t0 = time.time()
    white time.time() - t0 < 30:

    Использование:
    timebound = TimeBound()
    while timebound < 0.1:
    """

    def __init__(self):
        self.start_time = time.time()

    def __gt__(self, other):  # >
        return (time.time() - self.start_time) > other

    def __lt__(self, other):  # <
        return (time.time() - self.start_time) < other

    def __ge__(self, other):  # >=
        return (time.time() - self.start_time) >= other

    def __le__(self, other):  # <=
        return (time.time() - self.start_time) <= other


class Elapsed:
    """
    Замеряет время ОТ и ДО
    Использование:
    elapsed.start()
    time.sleep(1)
    elapsed.print('Fuck you')
    >> 19:22:09 |   DEBUG | Fuck you [1.0 sec]  timeutil.print:85

    elapsed.start()
    time.sleep(1)
    print(elapsed.result)
    >> [1.0 sec]
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
