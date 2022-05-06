# _*_coding:utf-8_*_
# @Time:2022/4/6 16:52
# @Author:Young
# @File:文件的序列化和反序列化


#dumps
# #创建一个文件
# fp = open('demo/text3.txt','w')
# name_list = ['zhangsan', 'lisi']
# import json
# #序列化
# #将python对象变成json字符串
# #我们在使用scrapy框架的时候  该框架会返回一个对象  我们要将对象写入到文件中就要使用json.dumps()
# names = json.dumps(name_list)
# #x写入到文件中
# fp.write(names)
# print(type(names))
# fp.close()


# #dump
# fp=open('text4.txt','w')
# name_list = ['zhangsan','lisi']
# import json
# #相当于 names=json.dumps(name_list)
# json.dump(name_list,fp)
# fp.close()


#反序列
#将json的字符串变成一个python对象
fp = open('demo/text3.txt', 'r')
content = fp.read()
# 读取之后是字符串
print(content)
print(type(content))
# loads
import json
# 将json字符串变成ypthon对象
result = json.loads(content)
# 装换之后
print(result)
print(type(result))
fp.close()

#load

# fp=open('demo/text3.txt','r')
# import json
# result = json.load(fp)
# print(result)
# print(type(result))
# fp.close()

