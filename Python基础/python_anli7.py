# _*_coding:utf-8_*_
# @Time:2022/4/23 15:48
# @Author:Young
# @File:python_anli7

# 题目：字符串日期转换为易读的日期格式。
import time
import parser
if __name__ == '__main__':
    # # 获取当前时间并转换为易读的日期:
    # # 1/获取当前时间戳
    # # time = time.time()
    # # print(time)
    # # 2/获取当前时间元组
    # localtime = time.localtime(time.time())
    # print(localtime)
    # # 3/获取格式化的时间
    # asctime =time.asctime(localtime)
    # # 4/输出格式化时间
    # print(asctime)
    localtime = time.asctime(time.localtime(time.time()))
    print("本地时间为 :", localtime)




