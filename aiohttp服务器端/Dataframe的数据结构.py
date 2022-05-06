# _*_coding:utf-8_*_
# @Time:2022/4/22 16:48
# @Author:Young
# @File:Dataframe的数据结构
import pandas
import pandas as pd

df = pd.read_excel('demo/1.xlsx')
# print(df.index)
print(type(df))
print(df.columns)
print(df.values)

# print(list(df.items()))

# for v in df.items():
#     print(v)
#     print('-----------------')