# _*_coding:utf-8_*_
# @Time:2022/4/6 18:03
# @Author:Young
# @File:爬虫_urllib_基本使用

#使用urllib来获取百度首页的源码

import urllib.request
#1、定义一个url  就是你访问的地址
url = 'http://www.baidu.com'

#2、模拟浏览器想服务器发送请求  response响应
response=urllib.request.urlopen(url)
#3、获取相应中的页面源码  content内容的意思
#read方法  返回的是字节形式的二进制数据
#  二进制--》字符串  解码  decode('编码的格式')
content = response.read().decode('utf-8')
 #4、打印数据
print(content)
