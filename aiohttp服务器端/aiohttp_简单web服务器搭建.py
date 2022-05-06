# _*_coding:utf-8_*_
# @Time:2022/4/15 15:27
# @Author:Young
# @File:aiohttp_简单web服务器搭建


# from aiohttp import web
# async def handle(request):
#     name = request.match_info.get('name', "Anonymous")
#     text = "Hello, " + name
#     return web.Response(text=text)
#
# app = web.Application()
# app.add_routes([web.get('/', handle),
#                 web.get('/{name}', handle)])
#
# web.run_app(app)


from aiohttp import web
import json
# 为了使一个web服务器生效，首先创建一个请求处理器  一个请求处理器必须是一个接受Request实例作为他唯一参数并且返回一个Response实例的协程：
async def hello(request):

    cont = 'hello Young'
    return web.Response(text=cont)


# async def hello2(request):
#     cont2 = 'hello Young2'
#     data = {
#
#         "validation": {
#             "access_token": "603f235a3aff97566b147c4e603f235a5050a3544"
#         },
#         "shipment": {
#             "shipment_id": "TS2204062485",
#             "client_reference": ""
#         }
#     }
#     return web.Response(json=data)
# 之后，创建一个Application实例并在特定的HTTP方法和路径上注册请求处理器：
app = web.Application()
app.add_routes([web.get('/', hello)])
# app.add_routes([web.get('/', hello2)])

# 然后，通过 run_app() 运行（最好指定下端口，不然可能会有进程已经占用默认端口）：
web.run_app(app, host='127.0.0.1', port=9000)
