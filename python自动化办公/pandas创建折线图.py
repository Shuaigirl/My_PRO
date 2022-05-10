# _*_coding:utf-8_*_
# @Time:2022/5/9 22:49
# @Author:Young
# @File:pandas创建折线图
import matplotlib.pyplot as plt
import pandas as pd

# 显示最大的列数·
# pd.options.display.max_columns=777
week = pd.read_excel("demo/test13.xlsx",index_col="Week")
print(week)
print(week.columns)
week.plot.area(y=['Accessories', 'Bikes', 'Clothing'])
# week.plot.bar(y=['Accessories', 'Bikes', 'Clothing'],stacked=True)
plt.title("Sales Weekly Trend",fontsize=16,fontweight="bold")
plt.ylabel("Total",fontsize=12,fontweight="bold")
plt.xticks(week.index,fontsize=8)
plt.show()