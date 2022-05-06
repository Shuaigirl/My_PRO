# _*_coding:utf-8_*_
# @Time:2022/4/19 10:31
# @Author:Young
# @File:aiohttp_异步爬虫小说排行

import asyncio
import csv

from aiohttp import ClientSession
from bs4 import BeautifulSoup


# 网站访问函数，将网站内容返回
async def getData(url, headers):
    # 创建回话对象
    async with ClientSession() as session:
        # 发送 get 请求，设置请求头
        async with session.get(url, headers=headers) as response:
            # 返回响应内容
            return await response.text()


def savaData(result):
    for i in result:
        soup = BeautifulSoup(i, 'lxml')
        find_div = soup.find_all('div', class_='book-mid-info')
        for d in find_div:
            # 小说名
            name = d.find('h2').getText()
            # 作者
            author = d.find('a', class_='name').getText()
            # 更新时间
            update = d.find('p', class_='update').getText()
            # 写入 csv
            csvFile = open('demo/data.csv', 'a', encoding='utf8', newline='')
            writer = csv.writer(csvFile)
            writer.writerow([name, author, update])
            csvFile.close()


def run():
    for i in range(25):
        # 构建不同的 url 传入 getData，最后由 asyncio 模块执行
        task = asyncio.ensure_future(getData(url.format(i + 1), headers))
        # 将所有请求都加入到列表 tasks
        tasks.append(task)
    # 等待所有请求执行完成，一并返回全部响应内容
    result = loop.run_until_complete(asyncio.gather(*tasks))
    savaData(result)
    print(len(result))


if __name__ == '__main__':
    import time

    start = time.time()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }
    tasks = []
    url = 'https://www.qidian.com/rank/hotsales?page={}'
    # 创建 get_evevt_loop 对象
    loop = asyncio.get_event_loop()
    # 调用 run 函数
    run()
    end = time.time()
    print(end - start)
