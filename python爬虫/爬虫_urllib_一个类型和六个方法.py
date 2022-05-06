# _*_coding:utf-8_*_
# @Time:2022/4/8 17:23
# @Author:Young
# @File:爬虫_urllib_一个类型和六个方法

import urllib.request
url = 'https://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
#response是HTTPResponse的一个类型
#print(type(response))

# 六个方法

# read()按一个一个字节去读
# content = response.read()
# print(content)

# read(5)返回多少个字节
# content = response.read(5)
# print(content)

# readline()读取一行
# content = response.readline()
# print(content)

# readline()读取一行
content = response.readlines()
print(content)

# getcode()返回状态码  如果状态码是200  则证明是逻辑没有问题
# print(response.getcode())

#geturl()返回url地址
# print(response.geturl())

#getheaders()返回一个状态信息
# print(response.getheaders())

#一个类型：HTTPResponse
#六个方法：read   readline  readlines  getcode  geturl  getheaders

