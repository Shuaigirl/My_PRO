# _*_coding:utf-8_*_
# @Time:2022/4/25 10:32
# @Author:Young
# @File:python_anli11
# 题目：输出 9*9 乘法口诀表。
# !/usr/bin/python3

for i in range(1, 10):
    print()
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j), end=" ")
