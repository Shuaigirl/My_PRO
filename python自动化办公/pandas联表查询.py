# _*_coding:utf-8_*_
# @Time:2022/5/10 12:07
# @Author:Young
# @File:pandas联表查询
import matplotlib.pyplot as plt
import pandas as pd
students = pd.read_excel("demo/test16.xlsx",sheet_name="student",index_col="ID")
scores = pd.read_excel("demo/test16.xlsx",sheet_name="score",index_col="ID")
table = students.merge(scores,how="left",on="ID").fillna(0)
table.Score = table.Score.astype(int)
print(table)
