# _*_coding:utf-8_*_
# @Time:2022/5/9 14:21
# @Author:Young
# @File:pandas筛选数据
import pandas as pd

def age_18_to_30(a):
    return 18<= a <30
def leval_a(s):
    return 85<= s <=100
students = pd.read_excel("demo/score.xlsx",index_col="ID")

# students = students.loc[students["age"].apply(age_18_to_30)].loc[students["score"].apply(leval_a)]# 第一种写法，调用方法名

# students = students.loc[students.age.apply(age_18_to_30)].loc[students.score.apply(leval_a)] #第二种写法,调用方法名

students = students.loc[students.age.apply(lambda a: 18<= a <30)] \
    .loc[students.score.apply(lambda s:85<= s <=100)] #第三种写法,行太长可以使用 "空格+\"

print(students)
