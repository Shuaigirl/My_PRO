# _*_coding:utf-8_*_
# @Time:2022/4/12 16:30
# @Author:Young
# @File:爬虫_requests_lxml获取百度一下

# 导入lxml库
# 解析本地文件：etree.parse("XX.html")
# 服务器响应文件：etree.HTML(response.read().decode('utf-8'))
# xpath路径：  tree.xpath(xpath路径)

from lxml import etree
# html_tree = etree.parse("爬虫_requests_lxml获取百度一下.html")
# html_tree = etree.HTML(html_tree.read().encode('utf-8'))
# 获取ul下面的li
# li_list = html_tree.xpath('//body/ul/li')
# print(li_list)

# 查找所有id的属性的li标签,text()获取内容
# li_list = html_tree.xpath('//ul/li[@id]/text()')
# print(li_list)

#找到id为l1的标签
# li_list = html_tree.xpath('//ul/li[@id="l1"]/text()')
# print(li_list)

# 查找id为l1的li标签的class的属性值
# li_list = html_tree.xpath('//ul/li[@id="l1"]/@class')
# print(li_list)

#打印标签的长度
# print(len(li_list))

#查找id中包含l开头的li标签
# li_list = html_tree.xpath('//ul/li[contains(@id,"l")]/text()')
# print(li_list)

#查找id的值以c开头的li标签值
# li_list = html_tree.xpath('//ul/li[starts-with(@id,"c")]/text()')
# print(li_list)

#查找id为l1以及class为c1的值
# li_list = html_tree.xpath('//ul/li[@id="l1" and @class="c1"]/text() ')
# print(li_list)

# 用requests 来爬取百度一下的文字
import  requests

url = 'https://www.baidu.com/'
headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
content = response.text
# print(content)
text = etree.HTML(content)
text_value = text.xpath('//input[@id="su"]/@value')
print(text_value)










