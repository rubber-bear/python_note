#  Task对象
import asyncio


# async def func1():
#     print(1)
#     await asyncio.sleep(4)
#     print(2)
#     return "就return一下返回值"
#
#
# async def main1():
#     print("main开始")
#     # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）。
#     task1 = asyncio.create_task(func1())
#     # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）。
#     task2 = asyncio.create_task(func1())
#     print("main结束")
#     # 当执行某协程遇到IO操作时，会自动化切换执行其他任务。
#     # 此处的await是等待相对应的协程全都执行完毕并获取结果
#     ret1 = await task1
#     ret2 = await task2
#     print(ret1, ret2)
#
# asyncio.run(main1())

"""
  **************************************************************************************
"""


async def func2():
    print(1)
    await asyncio.sleep(3)
    print(2)
    return "返回值"


async def main2():
    print("main_2开始")
    # 创建协程，将协程封装到Task对象中并添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）。
    # 在调用
    task_list = [
        asyncio.create_task(func2(), name="n1"),
        asyncio.create_task(func2(), name="n2")
    ]
    print("main_2结束")
    # 当执行某协程遇到IO操作时，会自动化切换执行其他任务。
    # 此处的await是等待所有协程执行完毕，并将所有协程的返回值保存到done
    # 如果设置了timeout值，则意味着此处最多等待的秒，完成的协程返回值写入到done中，未完成则写到pending中。
    done, pending = await asyncio.wait(task_list, timeout=2)
    print(done, pending)

asyncio.run(main2())

"""
  **************************************************************************************
"""


# async def func3():
#     print("执行协程函数内部代码")
#     # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
#     response = await asyncio.sleep(2)
#     print("IO请求结束，结果为：", response)
#
#
# coroutine_list = [func3(), func3()]
# # 错误：coroutine_list = [ asyncio.create_task(func()), asyncio.create_task(func()) ]
# # 此处不能直接 asyncio.create_task，因为将Task立即加入到事件循环的任务列表，
# # 但此时事件循环还未创建，所以会报错。
# # 使用asyncio.wait将列表封装为一个协程，并调用asyncio.run实现执行两个协程
# # asyncio.wait内部会对列表中的每个协程执行ensure_future，封装为Task对象。
# done, pending = asyncio.run(asyncio.wait(coroutine_list))
