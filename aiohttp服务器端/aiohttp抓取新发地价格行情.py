# _*_coding:utf-8_*_
# @Time:2022/4/21 9:31
# @Author:Young
# @File:aiohttp抓取新发地价格行情

import aiohttp
import asyncio
from aiohttp import ClientSession
import csv

async def getPrint(url, headers, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, data=data, headers=headers) as resp:
              return await resp.json()

if __name__ == '__main__':
   url = 'http://www.xinfadi.com.cn/priceDetail.html'
   headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
   }
   data = {
       "limit": 1,
       "current": 20
   }
   loop = asyncio.get_event_loop()
   loop.run_until_complete(getPrint(url=url, headers=headers, data=data))
