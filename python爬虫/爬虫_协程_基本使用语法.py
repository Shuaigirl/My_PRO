# _*_coding:utf-8_*_
# @Time:2022/4/13 14:41
# @Author:Young
# @File:爬虫_协程_基本使用语法



import asyncio
import time
# 基本案例一：
# async def func():
#     print('你好啊，我正在学习协程')
#
# if __name__ == '__main__':
#       g = func()   # 此时的函数是异步协程函数，执行的到是一个协程对象
#       # print(g)   这样会报错
#       asyncio.run(g)  # 协程程序需要asyncio模块的支持


#基本分析案例二：
# async def func1():
#     print('你好啊，我是Young')
#     # time.sleep(3)  # 当程序出现同步的时候，异步就中断了
#     await asyncio.sleep(3)  # 异步操作代码 await挂起切换到别的任务上
#     print('你好啊，我是Young')
#
# async def func2():
#         print('你好啊，我是Sanme')
#         # time.sleep(2)
#         await asyncio.sleep(2)
#         print('你好啊，我是Sanme')
#
# async def func3():
#     print('你好啊，我是YG')
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print('你好啊，我是YG')
#
# if __name__ == '__main__':
#     func1 = func1()
#     func2 = func2()
#     func3 = func3()
#     tasks = [
#         func1, func2, func3
#     ]
#     t1 = time.time()
#      #  一次性启动多个人任务（协程）
#     asyncio.run(asyncio.wait(tasks))
#     t2 = time.time()
#     print(t1)
#     print(t2)
#     print(t2-t1)

# 基本案例三：完善的几种写法
async def func1():
    print('你好啊，我是Young')
    await asyncio.sleep(3)
    print('你好啊，我是Young')

async def func2():
        print('你好啊，我是Sanme')
        await asyncio.sleep(2)
        print('你好啊，我是Sanme')

async def func3():
    print('你好啊，我是YG')
    await asyncio.sleep(4)
    print('你好啊，我是YG')

async  def main():
    #第一种写法：
    # f1 = func1()  # 一般await挂起操作放在协程对象前面
    # await f1
    #第二种写法（推荐）
    tasks = [
        func1(),
        func2(),
        func3()
    ]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    t1 = time.time()
    #  一次性启动多个人任务（协程）
    asyncio.run(main())
    t2 = time.time()
    print(t1)
    print(t2)
    print(t2-t1)
