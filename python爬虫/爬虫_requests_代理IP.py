# _*_coding:utf-8_*_
# @Time:2022/4/11 17:23
# @Author:Young
# @File:爬虫_requests_代理IP


import requests
import random
#url = 'https://www.baidu.com/?'

url = 'https://www.baidu.com/'

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
data = {
      'wd': 'IP',
}
# 代理池
proxies = {
    'http': '212.129.251.168:16816'
}
# print(proxies)
# proxies = random.choice(proxies)
# requests.get(url=路径，params=参数，headers=字典)
response = requests.get(url=url, params=data, headers=header, proxies=proxies)
content = response.text
print(content)

