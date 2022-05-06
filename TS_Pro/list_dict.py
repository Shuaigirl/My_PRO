# _*_coding:utf-8_*_
# @Time:2022/4/30 15:08
# @Author:Young
# @File:list_dict
data = {
                "validation": {
                         "access_token": "603f235a3aff97566b147c4e603f235a5050a3544"
                },
                "shipment": {
                    "service": "FBA-E232U",
                    "store_id": "",
                    "client_reference": "",
                    "reference_1": "",
                    "to_address": {
                                    "name": "hugh",
                                    "company": "wahaha llc",
                                    "tel": "1818181811",
                                    "mobile": "",
                                    "address_1": "2580 CORPORATE PLACE",
                                    "address_2": "SUITE#F107",
                                    "address_3": "",
                                    "city": "MONTEREY PARK",
                                    "state": "CA",
                                    "state_code": "CA",
                                    "country": "US",
                                    "postcode": "91754",
                                    "email": "",
                                    "validated": 0
                    },

                    "parcels": [{
                                    "number": "FBA16CV5TSBRU000001",
                                    "client_weight": "2",
                                    "client_length": "3",
                                    "client_width": "4",
                                    "client_height": "5"
                                },{
                                    "number": "FBA16CV5TSBRU000002",
                                    "client_weight": 13.08,
                                    "client_length": 60,
                                    "client_width": 52,
                                    "client_height": 39
                                }
                    ],
                    "declarations": [{
                                    "sku": "testsku",
                                    "name_zh": "zhongwenming",
                                    "name_en": "yingwenming",
                                    "unit_value": 11,
                                    "qty": 1,
                                    "material": "glass",
                                    "usage": "play",
                                    "brand": "",
                                    "parcel_number": "FBA16CV5TSBRU000001"
                                    },{
                                    "sku": "",
                                    "name_zh": "泡泡乐",
                                    "name_en": "Simple Popper Fidget Sensory Toys",
                                    "unit_value": "1.00",
                                    "qty": "90",
                                    "material": "plastic",
                                    "usage": "entertainment",
                                    "brand": "无",
                                    "parcel_number": "FBA16D3KMLYVU000002"
                                }]
            }
   }
print(data['shipment']['declarations'][0].get('sku'))