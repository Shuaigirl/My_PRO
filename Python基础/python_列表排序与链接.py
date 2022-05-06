# _*_coding:utf-8_*_
# @Time:2022/4/27 9:27
# @Author:Young
# @File:python_列表排序与链接
'''
题目：列表排序及连接。
程序分析：排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。
'''
a = [1,3,2 ]
a.sort()
print(a)
b = [7,4,5]
print(a+b)
a.extend(b)
print(a)