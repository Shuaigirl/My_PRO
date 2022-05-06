# _*_coding:utf-8_*_
# @Time:2022/4/19 15:37
# @Author:Young
# @File:ceshi
import requests

url = 'http://tiansheng.nextsls.com/api/v4/shipment/labels'
headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
data = {
                "validation": {
                    "access_token": "603f235a3aff97566b147c4e603f235a5050a3544"
                },
            #        # 创建运单
            #     "shipment": {
            #         "service": "FBA-EU",
            #         "store_id": "",
            #         "client_reference": "",
            #         "reference_1": "",
            #         "reference_2": "",
            #         "parcel_count": 2,
            #         "taxwith": 0,
            #         "deliverywith": "",
            #         "exportwith": 0,
            #         "importwith": 0,
            #         "attrs": [],
            #         "vat_number": "",
            #         "declaration_currency": "",
            #         "amazon_ref_id": "",
            #         "to_warehouse_code": "",
            #         "to_address": {
            #         "name": "hugh",
            #         "company": "wahaha llc",
            #         "tel": "1818181811",
            #         "mobile": "",
            #         "address_1": "2580 CORPORATE PLACE",
            #         "address_2": "SUITE#F107",
            #         "address_3": "",
            #         "city": "MONTEREY PARK",
            #         "state": "CA",
            #         "state_code": "CA",
            #         "country": "US",
            #         "postcode": "91754",
            #         "email": "",
            #         "validated": 0
            #         },
            #         "from_address": {
            #                         "name": "hugh",
            #                         "company": "wahaha llc",
            #                         "tel": "1818181811",
            #                         "mobile": "",
            #                         "address_1": "2580 CORPORATE PLACE",
            #                         "address_2": "SUITE#F107",
            #                         "address_3": "",
            #                         "city": "MONTEREY PARK",
            #                         "state": "CA",
            #                         "state_code": "CA",
            #                         "country": "US",
            #                         "postcode": "91754",
            #                         "email": ""
            #         },
            #         "parcels": [{
            #         "number": "FBA16CV5TSBRU000001",
            #         "client_weight": "2",
            #         "client_length": "3",
            #         "client_width": "4",
            #         "client_height": "5"
            #         }],
            #         "declarations": [{
            #         "sku": "testsku",
            #         "name_zh": "zhongwenming",
            #         "name_en": "yingwenming",
            #         "unit_value": 11,
            #         "qty": 1,
            #         "material": "glass",
            #         "usage": "play",
            #         "brand": "",
            #         "brand_type": "",
            #         "model": "",
            #         "purchase_price": 0,
            #         "sale_price": 0,
            #         "sale_url": "",
            #         "asin": "",
            #         "fnsku": "fnsku",
            #         "weight": 0,
            #         "size": "",
            #         "photo_url": "",
            #         "hscode": 1234567890,
            #         "duty_rate": 0,
            #         "photos": [],
            #         "is_battery": 0,
            #         "is_magnetic": 0 ,
            #         "battery_label": "",
            #         "battery_description": "",
            #         "title": "",
            #         "description": "",
            #         "platform": "",
            #         "amazon_ref_id": "",
            #         "parcel_number": "FBA16CV5TSBRU000001"
            #         }]
            # }

             "shipment": {
                    "shipment_id": "TS2203299444",
                    "client_reference": ""
                        }


    }
resp = requests.post(url=url, data=data)
print(resp.json())
