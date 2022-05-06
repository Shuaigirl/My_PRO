from aiohttp import web
import aiohttp
import json
routes = web.RouteTableDef()
# @routes.post('/api/v4/shipment/label')
# async def shipment_create(request):
#     req_json = await request.json()
#     print(req_json)
#     token = req_json["validation"]["access_token"]
#     print(token)
#     post_json = req_json
#
#     client_session = aiohttp.ClientSession(raise_for_status=True)
#     resp = await client_session.post("http://127.0.0.1:8082/api/v4/shipment/label", json=post_json)
#     async with resp:
#         x = await resp.json()
#         print(x)
#     await client_session.close()
#     return web.json_response(x)
async def Clintservices(url, post_json):
    async with aiohttp.ClientSession() as session:
         async  with session.post(url=url, json=post_json) as resp:
             # print(await resp.text())
             cont = await resp.json()
             return web.json_response(cont)


@routes.post('/api/v4/shipment/create')
async def ship_create(request):
    req_json = await request.json()
    print(req_json)
    # print(type(req_json))
    # print(req_json['validation'].get('access_token'))
    url = 'http://127.0.0.1:8082/api/v4/shipment/creat'
    # post_json = req_json

    # 1、添加字段：export_scc，import_scc
    req_json['shipment']['export_scc'] = 0
    req_json['shipment']['import_scc'] = 0
    req_json['shipment']['test'] = '测试字段'
    print(req_json)

    # 2、修改字段下的value值
    for i in req_json['shipment']:
        # print(i)
        if i == 'import_scc':
            print('这是我要修改的字段：', i)
            req_json['shipment'][i] = 1  # 这样只是修改import_scc字段的值为'1',而不是直接修改字段
            break

    # 3、删除字段
    del req_json['shipment']['test']



    post_json = req_json
    print(req_json)
    return await Clintservices(url, post_json)





    # json_list = open("demo/clinet.json", "rb")
    # post_json = json.load(json_list)
    # print(post_json)
    # print(type(post_json))
    # for req_json1, post_json1 in zip(sorted(req_json), sorted(post_json)):
    #    print(req_json1, post_json1)
    #    if req_json1 != post_json1:
    #        print("字段不相符：",req_json1, post_json1)
    #        if str(req_json[req_json1] != post_json[post_json1]):
    #            return await print("字段内容不相符：", req_json[req_json1],'\n',post_json[post_json1])
    #
    #    else:
    #        return await Clintservices(url, post_json)


app = web.Application()
app.add_routes(routes)
web.run_app(app)


