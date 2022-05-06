# _*_coding:utf-8_*_
# @Time:2022/4/25 12:00
# @Author:Young
# @File:python_条件判断分数的等级

'''
常见的格式化符号
格式符号	转换
%s	通过str()字符串转换来格式化
%u	无符号的十进制整数
%d	有符号的十进制整数
%o	八进制整数
%x	十六进制整数，小写字母
%X	十六进制整数，大写字母
%e	浮点数字(科学计数法)
%E	浮点数字(科学计数法，用E代替e)
%f	浮点实数
%g	浮点数字(根据值的大小采用%e或%f)
%G	浮点数字(类似于%g)
'''

score = int(input('请输入你的分数：'))
if score > 90:
    grade = 'A'
elif score > 60:
    grade = 'B'
else:
    grade = 'C'
print('%d属于%s等级!'%(score, grade))
