# _*_coding:utf-8_*_
# @Time:2022/4/13 15:20
# @Author:Young
# @File:爬虫_协程_应用领域

import asyncio
async def download():
    print('准备下载')
    await asyncio.sleep(2)  # 网络请求  requests.get()
    print('下载完成')
async def main():
    urls = [
        'http://www.baidu.com',
        'http://www.bilibili.com',
        'http://www.163.com'
        ]
    tasks = []
    for url in urls:
        d = download(tasks)
        tasks.append(d)

if __name__ == '__main__':
    asyncio.run(main())
