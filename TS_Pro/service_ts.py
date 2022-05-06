from aiohttp import web
import aiohttp


routes = web.RouteTableDef()

#构造供应商标准Json格式，并赋值
def CreatJson(req_json):
    access_token = req_json['validation'].get('access_token')
    service = req_json['shipment'].get('service')
    store_id = req_json['shipment'].get('store_id')
    client_reference = req_json['shipment'].get('client_reference')
    reference_1 = req_json['shipment'].get('reference_1')
    reference_2 = req_json['shipment'].get('reference_2')
    parcel_count = req_json['shipment'].get('parcel_count')
    # export_scc = req_json['shipment'].get('export_scc')
    # import_scc = req_json['shipment'].get('import_scc')
    taxwith = req_json['shipment'].get('taxwith')
    deliverywith = req_json['shipment'].get('deliverywith')
    exportwith = req_json['shipment'].get('exportwith')
    importwith = req_json['shipment'].get('importwith')
    attrs = req_json['shipment'].get('attrs')
    vat_number = req_json['shipment'].get('vat_number')
    declaration_currency = req_json['shipment'].get('declaration_currency')
    amazon_ref_id = req_json['shipment'].get('amazon_ref_id')
    to_warehouse_code = req_json['shipment'].get('to_warehouse_code')
    # from_address = req_json['shipment'].get('from_address')
    # to_address收件人地址
    # to_address = req_json['shipment'].get('to_address')
    t_name = req_json['shipment']['to_address'].get('name')
    t_company = req_json['shipment']['to_address'].get('company')
    t_tel = req_json['shipment']['to_address'].get('tel')
    t_mobile = req_json['shipment']['to_address'].get('mobile')
    t_address_1 = req_json['shipment']['to_address'].get('address_1')
    t_address_2 = req_json['shipment']['to_address'].get('address_2')
    t_address_3 = req_json['shipment']['to_address'].get('address_3')
    t_city = req_json['shipment']['to_address'].get('city')
    t_state = req_json['shipment']['to_address'].get('state')
    t_state_code = req_json['shipment']['to_address'].get('state_code')
    t_country = req_json['shipment']['to_address'].get('country')
    t_postcode = req_json['shipment']['to_address'].get('postcode')
    t_email = req_json['shipment']['to_address'].get('email')
    t_validated = req_json['shipment']['to_address'].get('validated')
    # print(t_name,t_company,t_tel,t_mobile,t_address_1,t_address_2,t_address_3,t_city,t_state,t_state_code,t_country,t_postcode,t_email,t_validated)
    # 获取from_address发件人地址
    f_name = req_json['shipment']['from_address'].get('name')
    f_company = req_json['shipment']['from_address'].get('company')
    f_tel = req_json['shipment']['from_address'].get('tel')
    f_mobile = req_json['shipment']['from_address'].get('mobile')
    f_address_1 = req_json['shipment']['from_address'].get('address_1')
    f_address_2 = req_json['shipment']['from_address'].get('address_2')
    f_address_3 = req_json['shipment']['from_address'].get('address_3')
    f_city = req_json['shipment']['from_address'].get('city')
    f_state = req_json['shipment']['from_address'].get('state')
    f_state_code = req_json['shipment']['from_address'].get('state_code')
    f_country = req_json['shipment']['from_address'].get('country')
    f_postcode = req_json['shipment']['from_address'].get('postcode')
    f_email = req_json['shipment']['from_address'].get('email')
    remark = req_json['shipment']['remark']
    # parcels数据获取
    parcel_data=[]
    parcels = req_json['shipment']['parcels']
    declarations= req_json['shipment']['declarations']
    for i in range(len(parcels)):
        number = parcels[i].get("number")
        client_weight=parcels[i].get("client_weight")
        client_length=parcels[i].get("client_length")
        client_width =parcels[i].get("client_width")
        client_height =parcels[i].get("client_height")
        d_data=[]
        for j in range(len(declarations)):
            parcel_number =declarations[j].get("parcel_number")
            sku=declarations[j].get("sku")
            name_zh=declarations[j].get("name_zh")
            name_en=declarations[j].get("name_en")
            d={
                "sku": sku,"name_zh": name_zh,"name_en": name_en
            }
            if number == parcel_number:
                d_data.append(d)
        data= {
           "number":number, "client_height":client_weight,"client_length":client_length,"client_width":client_width,"client_height":client_height,"declarations":d_data
        }
        parcel_data.append(data)


    post_json = {
                    "validation": {
                        "access_token": access_token
                    },
                    "shipment": {
                        "service": service,
                        "store_id": store_id,
                        "client_reference": client_reference,
                        "reference_1": reference_1,
                        "reference_2": reference_2,
                        "parcel_count": parcel_count,
                        "export_scc": 0,
                        "import_scc": 0,
                        "taxwith": taxwith,
                        "deliverywith": deliverywith,
                        "exportwith": exportwith,
                        "importwith": importwith,
                        "attrs": attrs,
                        "vat_number": vat_number,
                        "declaration_currency": declaration_currency,
                        "amazon_ref_id": amazon_ref_id,
                        "to_warehouse_code": to_warehouse_code,
                        "to_address": {
                            "name": t_name,
                            "company": t_company,
                            "tel": t_tel,
                            "mobile": t_mobile,
                            "address_1": t_address_1,
                            "address_2": t_address_2,
                            "address_3": t_address_3,
                            "city": t_city,
                            "state": t_state,
                            "state_code": t_state_code,
                            "country": t_country,
                            "postcode": t_postcode,
                            "email": t_email
                        },
                        "from_address" : {
                            "name": f_name,
                            "company": f_company,
                            "tel": f_tel,
                            "mobile": f_mobile,
                            "address_1": f_address_1,
                            "address_2": f_address_2,
                            "address_3": f_address_3,
                            "city": f_city,
                            "state": f_state,
                            "state_code": f_state_code,
                            "country": f_country,
                            "postcode": f_postcode,
                            "email": f_email
                        },

                        "parcels": parcel_data,
                        "remark": remark

                    }
        }
    return post_json

async def Clintservices(url,post_json,header):
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, data=post_json, headers=header) as resp:
            cont = await resp.json(content_type='text/json', encoding='utf-8')
            print(cont)
            return web.json_response(cont)
            # return web.json_response({'main':'ok'})

@routes.post('/api/v4/shipment/create')
async def ship_create(request):
    req_json = await request.json()
    url = 'http://tiansheng.nextsls.com/api/v4/shipment/creat'
    header = {
                'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 99.0.4844.51Safari / 537.36'
             }
    post_json = CreatJson(req_json)
    print(post_json)
    return await Clintservices(url, post_json, header)

app = web.Application()
app.add_routes(routes)
web.run_app(app)


