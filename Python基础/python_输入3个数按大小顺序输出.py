# _*_coding:utf-8_*_
# @Time:2022/4/27 10:07
# @Author:Young
# @File:python_输入3个数按大小顺序输出

def run(p1,p2):
    return p2,p1

if __name__ == '__main__':
    n1 = input('请输入一个数字')
    n2 = input('请输入一个数字')
    n3 = input('请输入一个数字')
    if n1 > n2:n1,n2 = run(n1,n2)
    if n1 > n3:n1,n3 = run(n1,n3)
    if n2 > n3:n2,n3 = run(n2,n3)
    print(n1,n2,n3)