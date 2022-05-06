# _*_coding:utf-8_*_
# @Time:2022/4/21 10:02
# @Author:Young
# @File:requests 获取新发地市场价格
import requests
import csv
import json
url = 'http://www.xinfadi.com.cn/getPriceData.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}
a = 1
while a <= 10:
    data = {
        "limit": 20,
        "current": a
    }
    resp = requests.post(url=url, data=data, headers=headers)
    cont = resp.json()
    a = a + 1
    # print(cont)
    for i in cont['list']:
        prodCat = i['prodCat']
        prodName = i['prodName']
        lowPrice = i['lowPrice']
        highPrice = i['highPrice']
        avgPrice = i['avgPrice']
        place = i['place']
        unitInfo = i['unitInfo']
        pubDate = i['pubDate']
        # print(prodName, place)
        fwriet =csv.writer(open("demo/price.csv", 'a', newline='', encoding='utf-8'))
        fwriet.writerow([prodCat, prodName, lowPrice, highPrice, avgPrice, place, unitInfo, pubDate])
