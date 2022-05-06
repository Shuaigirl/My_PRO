# _*_coding:utf-8_*_
# @Time:2022/4/22 15:27
# @Author:Young
# @File:pandas读取Excel文件

import pandas as pd
df = pd.read_excel('demo/1.xlsx')      # 默认读取的是第一个单元表
# df = pd.read_excel('demo/1.xlsx', 1)   # 同一表中的第二个单元表
# df = pd.read_excel('demo/1.xlsx', '表名')   # 同一表中直接填写表名
# print(df)
# 将读取后的数据  保存为另一个excel 表
df.to_excel('demo/2.xlsx')

