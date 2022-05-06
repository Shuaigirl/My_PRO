# _*_coding:utf-8_*_
# @Time:2022/4/19 15:08
# @Author:Young
# @File:pathon_anli3

'''
有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
'''
# !/usr/bin/python
#  第一种写法：
# -*- coding: UTF-8 -*-

# if __name__ == '__main__':
#     import string
#
#     fp = open('demo/text.txt')
#     a = fp.read()
#     fp.close()
#
#     fp = open('demo/text2.txt')
#     b = fp.read()
#     fp.close()
#
#     fp = open('demo/text3.txt', 'w')
#     l = list(a + b)
#     l.sort()
#     s = ''
#     s = s.join(l)
#     fp.write(s)
#     fp.close()

# 第二种写法：
with open('demo/text.txt') as f1, open('demo/text2.txt') as f2, open('demo/2.txt', 'w') as f3:
    for a in f1:
        b = f2.read()
        print(a,b)
    c = list(a + b)
    c.sort()
    print(c)
    d = ''  #
    d = d.join(c)
    f3.write(d)