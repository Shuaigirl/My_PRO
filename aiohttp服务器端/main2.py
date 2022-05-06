from aiohttp import web
import aiohttp

routes = web.RouteTableDef()
# @routes.post('/api/v4/shipment/label')
# async def shipment_create(request):
#     req_json = await request.json()
#     # print(req_json)
#     token = req_json["validation"]["access_token"]
#     return web.json_response({"erfd": "2dfgsdfgfd222222222222222222222222222222"})

@routes.post('/api/v4/shipment/creat')
async def shipment_create(request):
     j_list =await request.json()
     print(j_list)
     print(type(j_list))
     return  web.json_response({"main2:": "ok"})

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8082)


