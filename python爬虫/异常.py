# _*_coding:utf-8_*_
# @Time:2022/4/6 17:34
# @Author:Young
# @File:异常


#异常的格式
#try：坑可能出现异常的代码
#except异常的类型
#      友好提示
try:
    fp = open('demo/text.txt', 'r')
    fp.read()
except FloatingPointError:
    print('系统正在升级')
