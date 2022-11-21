# 伪代码
"""
任务列表 = [ 任务1, 任务2, 任务3,... ]
while True:
    可执行的任务列表，已完成的任务列表 = 去任务列表中检查所有的任务，将'可执行'和'已完成'的任务返回
    for 就绪任务 in 已准备就绪的任务列表:
        执行已就绪的任务
    for 已完成的任务 in 已完成的任务列表:
        在任务列表中移除 已完成的任务
    如果 任务列表 中的任务都已完成，则终止循环

    在编写程序时候可以通过如下代码来获取和创建事件循环。
    import asyncio
    loop = asyncio.get_event_loop()
"""

import asyncio


# 协程函数，定义形式为 async def 的函数
# 定义一个协程函数
# async def func():
#     pass
#
#
# # 调用协程函数，返回一个协程对象
# result = func()


# async def func1():
#     print("协程内部代码")
#
#
# # 调用协程函数，返回一个协程对象。
# result = func1()
# # 方式一
# loop = asyncio.get_event_loop()  # 创建一个事件循环
# loop.run_until_complete(result)  # 将协程当做任务提交到事件循环的任务列表中，协程执行完成之后终止。
# # 方式二
# # 本质上方式一是一样的，内部先 创建事件循环 然后执行 run_until_complete，一个简便的写法。
# # asyncio.run 函数在 Python 3.7 中加入 asyncio 模块，
# asyncio.run(result)
#
# # 将协程当做任务添加到 事件循环 的任务列表，然后事件循环检测列表中的协程是否 已准备就绪（默认可理解为就绪状态），如果准备就绪则执行其内部代码
#
# """
# await是一个只能在协程函数中使用的关键字，用于遇到IO操作时挂起 当前协程（任务），当前协程（任务）挂起过程中 事件循环可以去执行其他的协程（任务)，
# 当前协程IO处理完成时，可以再次切换回来执行await之后的代码
# """
#
#
# async def func2():
#     print("执行协程函数内部代码")
#     # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。
#     # 当前协程挂起时，事件循环可以去执行其他协程（任务）。
#     response = await asyncio.sleep(2)
#     print("IO请求结束，结果为：", response)
#
# result = func2()
# asyncio.run(result)


# async def others_1():
#     print("start")
#     await asyncio.sleep(2)
#     print('end')
#     return '返回值'
#
#
# async def func3():
#     print("执行协程函数内部代码")
#     # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
#     response = await others_1()
#     print("IO请求结束，结果为：", response)
#
#
# asyncio.run(func3())

# async def others_2():
#     print("start")
#     await asyncio.sleep(2)
#     print('end')
#     return '返回值'
#
#
# async def func4():
#     print("执行协程函数内部代码")
#     # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
#     response1 = await others_2()
#     print("IO请求结束，结果为：", response1)
#     response2 = await others_2()
#     print("IO请求结束，结果为：", response2)
#
#
# asyncio.run(func4())
