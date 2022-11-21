"""
asyncio，得先了解协程，协程是根本
# 协程（Coroutine），也可以被称为微线程，是一种用户态内的上下文切换技术。简而言之，其实就是通过一个线程实现代码块相互切换执行
def func1():
    print(1)
    ...
    print(2)


def func2():
    print(3)
    ...
    print(4)

# 若想输出 1, 3, 2, 4

在Python中有多种方式可以实现协程，例如：
    greenlet，是一个第三方模块，用于实现协程代码（Gevent协程就是基于greenlet实现）
    yield，生成器，借助生成器的特点也可以实现协程代码。
    asyncio，在Python3.4 中引入的模块用于编写协程代码。
    async & await，在Python3.5 中引入的两个关键字，结合asyncio模块可以更方便的编写协程代码。

"""

#
# def func1():
#     print(1)
#     ...
#     print(2)
#
#
# def func2():
#     print(3)
#     ...
#     print(4)


# 若想输出 1, 3, 2, 4

# 在Python中有多种方式可以实现协程，例如：
#     greenlet，是一个第三方模块，用于实现协程代码（Gevent协程就是基于greenlet实现）
#     yield，生成器，借助生成器的特点也可以实现协程代码。
#     asyncio，在Python3.4 中引入的模块用于编写协程代码。
#     async & await，在Python3.5 中引入的两个关键字，结合asyncio模块可以更方便的编写协程代码。


# greenlet
# from greenlet import greenlet
#
#
# def func1():
#     print(1)  # 第1步：输出 1
#     gr2.switch()  # 第3步：切换到 func2 函数
#     print(2)  # 第6步：输出 2
#     gr2.switch()  # 第7步：切换到 func2 函数，从上一次执行的位置继续向后执行
#
#
# def func2():
#     print(3)  # 第4步：输出 3
#     gr1.switch()  # 第5步：切换到 func1 函数，从上一次执行的位置继续向后执行
#     print(4)  # 第8步：输出 4
#
#
# gr1 = greenlet(func1)
# gr2 = greenlet(func2)
# gr1.switch()  # 第1步：去执行 func1 函数


# # ********************************************************************
# def func3():
#     yield 1
#     yield from func4()
#     yield 2
#
#
# def func4():
#     yield 3
#     yield 4
#
#
# f3 = func3()
# for item in f3:
#     print(item)
#
# # ********************************************************************************
# async & await 关键字在Python3.5版本中正式引入，基于他编写的协程代码其实就是 上一示例 的加强版，让代码可以更加简便。


# @asyncio.coroutine
# def func1():
#     print(1)
#     yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其他任务
#     print(2)
#
#
# @asyncio.coroutine
# def func2():
#     print(3)
#     yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其他任务
#     print(4)
#
#
# tasks = [
#     asyncio.ensure_future(func1()),
#     asyncio.ensure_future(func2())
# ]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))


import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
