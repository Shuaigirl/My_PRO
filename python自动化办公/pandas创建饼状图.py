# _*_coding:utf-8_*_
# @Time:2022/5/9 17:13
# @Author:Young
# @File:pandas创建饼状图
import matplotlib.pyplot as plt
import pandas as pd
fp = pd.read_excel("demo/test12.xlsx",index_col="From")
print(fp)
fp["2017"].plot.pie(fontsize=8, counterclock=False,)
plt.title("Source of International Student",fontsize=16,fontweight="bold")
plt.ylabel("2017",fontsize=12,fontweight="bold")
plt.show()