"""
装饰器：
    在python中函数只不过是一个普通的对象， 函数也可以作为参数传进其他的函数里、函数的返回值也可以是一个函数
    decorator 是一个输入和输出都是函数的函数
    闭包：
        在闭包中,由于内部函数存在对外部函数变量的引用,所以即使外部函数执行完毕,该变量依然存在
        但是一定是内层函数调用的外层函数的变量，如果内层函数不会引用，那么这个变量也是不存在的

    闭包有3个特性:
        函数嵌套函数;
        函数内部可以引用函数外部的参数和变量;
        参数和变量不会被垃圾回收机制回收.

"""

import time


def time_1(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        end = time.time()
        print("func %s spend %s" % (f.__name__, (end - start)))
        return ret

    return wrapper


def time_2(x):
    def wrapper(func):
        def inner(*args, **kwargs):
            start = time.time()
            for _ in range(x):
                ret = func(*args, **kwargs)
            end = time.time()
            print("func f spend %s" % (end - start))

        return inner

    return wrapper


@time_1
def func_1(x):
    print(x)


@time_2(10)
def func_2(m):
    return m ** 2


func_1(1)
# print(func_1.__name__)
# inner = time_2(10)
# func_2 = inner(func2)
