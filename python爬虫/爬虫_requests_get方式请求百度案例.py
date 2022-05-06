# _*_coding:utf-8_*_
# @Time:2022/4/11 16:32
# @Author:Young
# @File:爬虫_requests_get方式请求百度案例

import requests

#url = 'https://www.baidu.com/?'

url = 'https://www.baidu.com/'

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
data = {
      'wd': '北京',
      'tn': '25017023_15_pg'
}
# name = input('请输入你要搜素的内容：')
# new_url = f'https://www.baidu.com/s?wd={name}'
# print(new_url)
# requests.get(url=路径，params=参数，headers=字典)
response = requests.get(url=url, params=data, headers=header)


# 打印路径就知道请求资源路径中的？可加可不加
# print(response.url)
#输出结果：https://www.baidu.com/?wd=%E5%8C%97%E4%BA%AC&tn=25017023_15_pg



content = response.text
print(content)


# 总结：requests和urblib的区别
# 1、参数使用params传递
# 2、参数无需urlencode编码
# 3、不需要请求对象的定制
# 4、请求资源路径中的？可加可不加



'''
方法二：
import requests
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
name = input('请输入你要搜素的内容：')
new_url = f'https://www.baidu.com/s?wd={name}'
print(new_url)
response = requests.get(url=new_url, headers=header)
content = response.text
print(content)
'''
