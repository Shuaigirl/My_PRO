# _*_coding:utf-8_*_
# @Time:2022/4/11 12:03
# @Author:Young
# @File:爬虫_aiohttp_客户端实例2


#案例一：
# import asyncio
# # 协程（协程不是一个函数）
# async def print_hello():
#     while True:
#         print('Hello  Young')
#         await asyncio.sleep(1)   # 暂停1秒
# async def print_Goodbye():
#     while True:
#         print('Goodbye  Young')
#         await asyncio.sleep(2)   # 暂停2秒
# # 创建协程对象
# co = print_hello()
# co2 =print_Goodbye()
# # 获取事件循环
# loop = asyncio.get_event_loop()
# # 监听事件循环
# #loop.run_until_complete(co)
# loop.run_until_complete(asyncio.gather(co, co2))


#案例二：
import asyncio
import random

async def cron_scheduler():
    page = 1
    while True:
        url = '{}/{}'.format('https://www.baidu.com', page)
        job = cron_job(url)
        await job
        page = page+1


async def cron_job(url):
    n = random.randint(1, 3)
    await asyncio.sleep(n)
    print('下载结束：', url)

asyncio.run(cron_scheduler())
