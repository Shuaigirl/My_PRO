# _*_coding:utf-8_*_
# @Time:2022/4/23 17:44
# @Author:Young
# @File:python_anliq0
# 输入三个整数x,y,z，请把这三个数由小到大输出。
# !/usr/bin/python3
# 方法一：sort方法排序 输出列表
# l = []
# for i in range(3):
#     x = int(input('integer:\n'))
#     l.append(x)
# l.sort()
#
# for i in l:
#     print(i)

# 方法二：
l =[]
for i in range(6):
    num = int(input('请输入六个任意的数字：\n'))
    l.append(num)
l.sort()
print(l)












