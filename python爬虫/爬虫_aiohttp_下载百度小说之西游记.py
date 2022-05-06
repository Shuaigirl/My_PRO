# _*_coding:utf-8_*_
# @Time:2022/4/14 15:23
# @Author:Young
# @File:爬虫_aiohttp_下载百度小说之西游记

#  https://dushu.baidu.com/pc/detail?gid=4306063500
#  https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"} 可以获取到名称name/章节的cid
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}  可以获取到章节的内容

# 分 析：
# 1. 同步操作:访问getCatalog()获取所有章节名称和cid
# 2. 异步操作：访问getChapterContent（）获取所有章节的内容
import asyncio
import requests
import json
import aiohttp
import aiofiles

# 异步操作下载所有章节内容
async def getChapterContent(cid, b_id, title):

    data = {
        "book_id": b_id,
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1
    }

    # data 现在是要给json 先导入json 然后转换为字符串,loads()是字符串转换为json ;dumps()反序列由json转换为字符串
    data = json.dumps(data)
    headers = {
        'User-Agent':'Mozilla /5.0(Windows NT 10.0;Win64;x64) AppleWebKit /537.36(KHTML, likeGecko) Chrome/99.0.4844.51Safari/537.3'
    }
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    # print(url) # 获取到所有章节的链接
    async with aiohttp.ClientSession() as session:    # aiohttp.ClientSession()相当于requests
        async with session.get(url=url, headers=headers) as resp:
            dict = await resp.json()
            # print(dict['data']['noval']['chapter_title'])
            # dict['data']['noval']['content']用json来获取章节内容
            async with aiofiles.open("demo2/"+title+".txt", mode='w', encoding='utf-8') as f:
                await f.write(dict['data']['novel']['content'])  # 把章节内容写出到文件



# 同步操作下载所有章节名称和cid
async def getCatalog(url):
    response = requests.get(url)
    # print(response.text)
    dict = response.json()
    tasks = []
    for item in dict['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        # print(title, cid)
        # 拿到了所有的章节名称和cid 下一步就是获取章节内容，准备异步操作任务
        tasks.append(getChapterContent(cid, b_id, title))
    await asyncio.wait(tasks)
    # 或者这样写：asyncion.run(asyncio.wait(tasks))


if __name__ == '__main__':
    b_id = '4306063500'
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    # getCatalog(url)
    # asyncio.run()会自动关闭循环,并且调用_ProactorBasePipeTransport.__del__报错, 而asyncio.run_until_complete()不会.
    # asyncio.run(getCatalog(url))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getCatalog(url))
