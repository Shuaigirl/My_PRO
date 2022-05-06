# _*_coding:utf-8_*_
# @Time:2022/4/27 10:34
# @Author:Young
# @File:python_查找字符
'''
Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
'''

str1 = 'wo aini jiuxiang lao shu ai dami '
str3 = 'wo aini jiuxiang laoshu ai dami '
str2 = 'laoshu'
print(str1.find(str2))
print(str3.find(str2))
