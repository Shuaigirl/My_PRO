# _*_coding:utf-8_*_
# @Time:2022/4/19 15:30
# @Author:Young
# @File:python_anli4
'''
题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
字符串方法：str.upper()大写转换为小写 str.lower(）转换 string 中所有大写字符为小写.
'''

num = input('请输入你需要的字母：')
UpperNum = num.upper()
print(UpperNum)

with open('demo/anli4.txt','a',encoding='utf-8') as fp:
      fp. write(UpperNum)
      fp.close()
