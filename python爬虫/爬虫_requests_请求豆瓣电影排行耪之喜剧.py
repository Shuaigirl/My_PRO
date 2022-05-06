# _*_coding:utf-8_*_
# @Time:2022/4/15 12:04
# @Author:Young
# @File:爬虫_requests_请求豆瓣电影排行耪之喜剧
import requests

url = 'https://movie.douban.com/j/chart/top_list'
param = {
            'type': 24,
            'interval_id': '100:90',
            'action': '',
            'start': 0,
            'limit': 20
}
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
resp = requests.get(url=url, params=param, headers=header)
content = resp.json()
# print(resp.url)
# print(content)
