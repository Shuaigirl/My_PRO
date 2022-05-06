# _*_coding:utf-8_*_
# @Time:2022/4/27 10:38
# @Author:Young
# @File:python_打印杨辉三角
# 题目：打印出杨辉三角形

if __name__ == '__main__':
    a = []
    for i in range(10):
        a.append([])
        for j in range(10):
            a[i].append(0)
    for i in range(10):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2, 10):
        for j in range(1, i):
            a[i][j] = a[i - 1][j-1] + a[i - 1][j]
    from sys import stdout
    for i in range(10):
        for j in range(i + 1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print()

