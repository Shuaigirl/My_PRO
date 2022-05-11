# _*_coding:utf-8_*_
# @Time:2022/5/11 9:42
# @Author:Young
# @File:pandas查找重复项
import pandas as pd

student = pd.read_excel("demo/test20.xlsx",index_col="ID")
dupe = student.duplicated(subset="Name")
dupe = dupe[dupe]
print(student.iloc[dupe.index])