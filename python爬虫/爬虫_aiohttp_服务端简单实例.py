# _*_coding:utf-8_*_
# @Time:2022/4/11 11:18
# @Author:Young
# @File:爬虫_aiohttp_服务端简单实例

from aiohttp import web

# 服务端案例一：
# async def hello(request):
#     return web.Response(text="Hello, world")
# app = web.Application()
# app.add_routes([web.get('/', hello)])
# web.run_app(app)
# routes = web.RouteTableDef()

# async def handle(request):
#     name = request.match_info.get('name', "Young")
#     text = "Hello, " + name
#     return web.Response(text=text)
#
# app = web.Application()
# app.add_routes([web.get('/', handle), web.get('/{name}', handle)])
#
# if __name__ == '__main__':
#     web.run_app(app)


import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
