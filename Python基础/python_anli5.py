# _*_coding:utf-8_*_
# @Time:2022/4/23 15:16
# @Author:Young
# @File:python_anli5
#从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

# from sys import stdout
# if __name__ == '__main__':
#     fname = input('请输入文件名：')
#     fp = open('demo/'+fname, 'w', encoding='utf-8')
#     str = input('请输入字符串：')
#     while(str != '#'):
#         fp.write(str)
#         stdout.write(str)
#         str = input('')
#     fp.close()

#!/usr/bin/python3

filename = input('输入文件名:\n')
fp = open('demo/'+filename, "w+")
ch = ''
while '#' not in ch:
    fp.write(ch)
    ch = input('输入字符串:\n')
fp.close()
