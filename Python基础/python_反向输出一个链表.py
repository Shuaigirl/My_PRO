# _*_coding:utf-8_*_
# @Time:2022/4/27 9:47
# @Author:Young
# @File:python_反向输出一个链表
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 创建一个链表,然后反向输出
if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(input('please input a number:\n'))
        ptr.append(num)
    print(ptr)
    ptr.reverse()
    print(ptr)
