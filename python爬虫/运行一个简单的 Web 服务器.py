#  异步请求

import aiohttp
import asyncio


# 案例二：
# import aiohttp
# import asyncio
#
# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text(), response.status
#
# async def  main():
#     async with aiohttp.ClientSession() as session:
#         html, status = await fetch(session, 'https://www.baidu.com')
#         print(f'html:{html[:100]}...')
#         print(f'status:{status}')
#
# if __name__=='__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())

# 案例三：
# 定义main函数
async def main():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
           async with session.get('http://www.baidu.com', data=data) as response:
            #print(await response.text())
            print('status:',response.status)
            print('headers:',response.headers)
            print('body:',await response.text())
            print('bytes:',response.read())
            print('json:',response.json())


# 程序的入口：
if __name__=='__main__':
    asyncio.get_event_loop().run_until_complete(main())


















