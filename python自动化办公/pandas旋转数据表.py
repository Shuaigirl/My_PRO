# _*_coding:utf-8_*_
# @Time:2022/5/11 10:13
# @Author:Young
# @File:pandas旋转数据表
import pandas as pd
pd.options.display.max_columns = 999 #显示最大的列为999列
m = pd.read_excel("demo/test21.xlsx",index_col="Month")
table = m.transpose()
print(table)