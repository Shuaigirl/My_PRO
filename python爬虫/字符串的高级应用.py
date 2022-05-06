# _*_coding:utf-8_*_
# @Time:2022/4/1 16:40
# @Author:Young
# @File:字符串的高级应用

#len()长度
a='china'
print(len(a))
#find查找内容：变量.fine（'查找的内容'）,返回第一个查找内容的下标
a1='chiana'
print(a1.find('a'))
#判断：startswith,endswith 判断字符串是不是以谁睡开始或结束  返回True或者false
a2='chianasa'
print(a2.startswith('e'))
print(a2.endswith('a'))
#计算出现的次数：count
a3='chainads'
print(a3.count('a'))
#replaced代替
a4='chainads'
print(a4.replace('a','b'))
#切割字符串：split;返回的数组
a5='1*2*3*4*5'
print(a5.split('*'))
#修改大小写：upper,lower 主要运用于验证码
a6='china'
a7='CHIUHS'
print(a6.upper())
print(a7.lower())
#空格处理：strip,把空格去掉返回实际长度
a8='    a  a   '
print(a8.split())
print(len(a8.split()))
#字符串拼接：join,把hello插入到每个字符串中后面的结束
a9='o'
print(a9.join('qqqqqq'))