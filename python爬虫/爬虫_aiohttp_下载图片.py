# _*_coding:utf-8_*_
# @Time:2022/4/11 15:08
# @Author:Young
# @File:爬虫_aiohttp_下载图片

import asyncio
import aiohttp

urls = [
      'https://scpic.chinaz.net/files/pic/pic9/202204/apic40099.jpg',
      'https://scpic.chinaz.net/files/pic/pic9/202204/hpic5267.jpg',
      'https://scpic.chinaz.net/files/pic/pic9/202204/apic40088.jpg'
]

async def aiodownload(url):
    name = url.rsplit('/', 1)[1]  # 从右边切一次，得到[1]的位置内容
    async with aiohttp.ClientSession() as session:     # session相当于requests
        async with session.get(url) as resp:           # resp相当于requests.get()
            with open('demo/'+name, mode='wb') as fp:
                 #读取内容是异步的，需要await挂起
                fp.write(await resp.content.read())
    print(name, '下载好了')

async def main():
    # 创建任务对象
    tasks = []
    for url in urls:
        # append追加任务协程
        tasks.append(aiodownload(url))
    #   asyncio.wait启动任务列表
    await asyncio.wait(tasks)

if __name__ == '__main__':
    #asyncio.run(main())  #这样写报错： untimeError(‘Event loop is closed’) RuntimeError: Event loop is closed
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
