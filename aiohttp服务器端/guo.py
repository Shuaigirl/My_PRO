# _*_coding:utf-8_*_
# @Time:2022/4/21 11:05
# @Author:Young
# @File:guo.




import json
import csv
##直接获取json
# json_list = open("demo/guo.json", "rb")
# post_json = json.load(json_list)
# print(post_json)
# print(type(post_json))
# for i in post_json['data']['list']['vlist']:
#     pic = i['pic']
#     title = i['title']
#     aid = i['aid']
#     bvid = i['bvid']
#     created = i['created']
#     write = csv.writer(open('demo/guo.csv', 'a', encoding='utf-8'))
#     write.writerow([pic,title,aid,bvid,created])

import requests
# 网站直接获取json
url = 'https://api.bilibili.com/x/space/arc/search?mid=946974&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
resp = requests.get(url=url)
json_list = resp.json()
# print(json_list)
# print(type(json_list))
post_json = json_list
for i in post_json['data']['list']['vlist']:
    pic = i['pic']
    title = i['title']
    aid = i['aid']
    bvid = i['bvid']
    created = i['created']
    write = csv.writer(open('demo/guo2.csv', 'a', newline='', encoding='utf-8'))
    write.writerow([pic, title, aid, bvid, created])

