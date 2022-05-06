# _*_coding:utf-8_*_
# @Time:2022/4/11 17:03
# @Author:Young
# @File:爬虫_requests_post请求白百度翻译

import requests
import json

#url = 'https://www.baidu.com/?'

post_url = 'https://fanyi.baidu.com/sug'

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
#  name=input('请输入你要翻译的内容：')
data = {
      'kw': 'eye',
      # 'kw':name
}
# requests.post(url=路径，data=参数，headers=字典)
response = requests.post(url=post_url, data=data, headers=header)

content = response.text
# content = response.json()  #  直接获取json就不会乱码
# print(content)


#另一种方法转换为json
obg_json = json.loads(content.encode('utf-8'))
print(obg_json)


# 总结：requests和urllib的区别
# 1、get请求的参数是param=‘’,而post的请求参数是data=‘’；
# 2、请求资源的路径后面可以不加？
# 3、不需要手动编解码
# 4、不需要做请求对象的定制
