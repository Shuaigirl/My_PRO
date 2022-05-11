# _*_coding:utf-8_*_
# @Time:2022/5/10 17:30
# @Author:Young
# @File:pandas按某个条件分列
import pandas as pd

name = pd.read_excel("demo/test18.xlsx", index_col="ID")
df = name["Full Name"].str.split(expand=True)
name["First Name"] = df[0]
name["last Name"] = df[1].str.upper()
print(name)
