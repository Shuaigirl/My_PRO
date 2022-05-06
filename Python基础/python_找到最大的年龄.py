# _*_coding:utf-8_*_
# @Time:2022/4/26 9:29
# @Author:Young
# @File:python_找到最大的年龄

person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22, "hao": 59}
def find_max(dict):
    max_age = 0
    for key, value in dict.items():
        if value > max_age:
            max_age = value
            name = key
    print(name)
    print(max_age)
find_max(person)