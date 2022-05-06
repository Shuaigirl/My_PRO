# _*_coding:utf-8_*_
# @Time:2022/4/8 16:33
# @Author:Young
# @File:爬虫_urllib_请求对象的定制
import urllib.request
url = 'https://www.baidu.com/s?tn=25017023_15_pg&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'
#  url的组成
#   http/https   www.baodu.com     80/443     s      wd       #
#      协议            主机           端口     路径    参数      瞄点
# http  80
# https  443
# myql   3306
# oracle  1521
# redis   6379
# mongodb  27017
headers={
    'user-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
#1、请求对象的定制
request=urllib.request.Request(url=url,headers=headers)
#2、模拟浏览器想服务器发送请求  response相应
response = urllib.request.urlopen(request)
#3、输出中文编码
content = response.read().decode('utf-8')
print(content)







