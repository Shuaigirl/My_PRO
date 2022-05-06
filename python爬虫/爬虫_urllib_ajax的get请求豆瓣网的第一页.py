# _*_coding:utf-8_*_
# @Time:2022/4/9 14:19
# @Author:Young
# @File:爬虫_urllib_ajax的get请求豆瓣网的第一页

import urllib.request
import  urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20'
headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36X'
}
#  请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取数据
content = response.read().decode('utf-8')
# 写入到文件demo/douban.json
# open默认的情况下使用的是gbk编码，如果要保存为汉字那么encoding的编码就要设置为utf-8
# encoding = 'utf-8'
# 写入文件的第一种写法
# fp = open('demo/douban.json', 'w', encoding='utf-8')
# fp.write(content)
# 写入文件的第二种写法
with open('demo/douban3.json', 'w', encoding='utf-8') as fp:
 fp.write(content)
fp.close()
