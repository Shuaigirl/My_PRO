# _*_coding:utf-8_*_
# @Time:2022/4/11 10:57
# @Author:Young
# @File:爬虫_aiohttp_客户端简单实例
import aiohttp
import asyncio

# 定义一个协程（协程不是函数）
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

#
# 一个协程用来下载网页
async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "http://httpbin.org/headers")
        print(html)

# 程序入口
asyncio.run(main())


# url = 'http://httpbin.org/headers'
# session = aiohttp.ClientSession()
# response = session.get(url)
# text = response.text()
# print(text)



"""输出结果：
{
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "Python/3.7 aiohttp/3.6.2"
  }
}
"""