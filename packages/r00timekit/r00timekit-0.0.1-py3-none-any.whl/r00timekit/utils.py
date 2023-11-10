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
    Замена блока кода:
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
