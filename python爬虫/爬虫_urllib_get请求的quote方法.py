# _*_coding:utf-8_*_
# @Time:2022/4/8 16:33
# @Author:Young
# @File:爬虫_urllib_请求对象的定制
import urllib.request
import urllib.parse
url = 'https://www.baidu.com/s?wd='


headers={
    'user-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
name = urllib.parse.quote('周杰伦')
print(name)
new_url = url+name

request = urllib.request.Request(url=url, headers=headers)
#2、模拟浏览器想服务器发送请求  response相应
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)







