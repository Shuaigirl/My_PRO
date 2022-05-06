# _*_coding:utf-8_*_
# @Time:2022/4/22 15:54
# @Author:Young
# @File:csv文件的读取与保存
import pandas as pd

df = pd.read_csv('demo/guo2.csv')
print(df)
# df.to_csv('demo/guo3.csv', index=0)
df.to_csv('demo/guo3.xlsx', index=0)
