# _*_coding:utf-8_*_
# @Time:2022/4/27 13:33
# @Author:Young
# @File:t2
dict = {
                 "validation": {
                 "access_token": "603f235a3aff97566b147c4e603f235a5050a3544"
                },
                "shipment": {
                    "service": "FBA-EU",
                    "store_id": "",
                    "client_reference": "",
                    "city": "MONTEREY PARK",
                    "email": "",
                    "validated": 0
                    },
                    "from_address": {
                                    "name": "hugh",
                                    "company": "wahaha llc",
                                    "tel": "1818181811",
                                    "mobile": "",
                                    "address_1": "2580 CORPORATE PLACE",
                                    "address_2": "SUITE#F107",
                                    "email": ""
                    },
                    "parcels": [{
                                    "number": "FBA16CV5TSBRU000001",
                                    "client_weight": "2",
                                    "client_length": "3",
                                    "client_width": "4",
                                    "client_height": "5"
                    }]


    }

dict['shipment']["service2"] = dict['shipment'].pop('service')

print(dict)
