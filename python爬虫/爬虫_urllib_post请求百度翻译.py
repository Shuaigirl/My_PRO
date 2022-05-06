# _*_coding:utf-8_*_
# @Time:2022/4/9 10:30
# @Author:Young
# @File:爬虫_urllib_post请求百度翻译


import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/translate'

headers = {
    'user-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

data = {
         'kw': 'spider'
}

# post请求的参数，必须进行编码encode()
data = urllib.parse.urlencode(data).encode('utf-8')

# post的请求参数，是不会拼接在url后面的，而是需要放在请求对象的定制中
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取发送的内容,decode()解码
content = response.read().decode('utf-8')
print(content)

# # 字符串--》json对象
# obj = json.dumps(content)
# print(obj)


