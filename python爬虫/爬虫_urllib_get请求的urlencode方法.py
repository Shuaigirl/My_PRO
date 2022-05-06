# _*_coding:utf-8_*_
# @Time:2022/4/8 17:01
# @Author:Young
# @File:爬虫_urllib_get请求的urlencode方法
import urllib.request
import urllib.parse
base_url = 'https://www.baidu.com/s?'
data={
    'wd': '周杰伦',
    'tn': '25017023_15_pg',
    'sex': '男'
}
new_url = urllib.parse.urlencode(data)
# print(new_url)
url = base_url+new_url
headers={
    'user-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取数据
content = response.read().decode('utf-8')
print(content)
