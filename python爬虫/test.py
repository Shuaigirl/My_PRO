# _*_coding:utf-8_*_
# @Time:2022/4/14 10:03
# @Author:Young
# @File:test

import requests
import json
url = 'http://tiansheng.nextsls.com/api/v4/shipment/account'
headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
data = {
                "validation": {
                    "access_token": "603f235a3aff97566b147c4e603f235a5050a3544"
                },
                 # "shipment": {
                 #    "shipment_id": "TS2204062485",
                 #    "client_reference": ""
                 #  }
}

response = requests.post(url=url, headers=headers, json=data)
content = response.json()
# print(content)

print(content)
print(type(content))


