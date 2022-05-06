# _*_coding:utf-8_*_
# @Time:2022/4/25 14:12
# @Author:Young
# @File:python_统计出其中英文字母、空格、数字和其它字符的个数


'''

Python字符串检测方法

.isalnum()  所有字符都是数字或者字母，为真返回 Ture，否则返回 False。

.isalpha()   所有字符都是字母，为真返回 Ture，否则返回 False。

.isdigit()     所有字符都是数字，为真返回 Ture，否则返回 False。

.islower()    所有字符都是小写，为真返回 Ture，否则返回 False。

.isupper()   所有字符都是大写，为真返回 Ture，否则返回 False。

.istitle()      所有单词都是首字母大写，为真返回 Ture，否则返回 False。

.isspace()   所有字符都是空白字符，为真返回 Ture，否则返回 False。

'''

import string
s = input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print ('char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others))