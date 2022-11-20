"""
计算时间
"""

import time


def timeit(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s func running %s sec" % (func.__name__, (t2 - t1)))
        return result
    return wrapper