# _*_coding:utf-8_*_
# @Time:2022/4/11 16:12
# @Author:Young
# @File:爬虫_requests_基本用法

import requests

# 一个类型和六个属性:

url = 'https://www.baidu.com'
response = requests.get(url=url)

# 返回'requests.models.Response'>类型
print(type(response))

# 设置响应的编码
response.encoding = 'utf-8'

# 以字符串的形式来返回网页的源码
content = response.text
print(content)

# 返回一个url地址
print(response.url)

# 返回状态码
print(response.status_code)

# 返回响应头
print(response.headers)