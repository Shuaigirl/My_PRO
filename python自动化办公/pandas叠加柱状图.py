# _*_coding:utf-8_*_
# @Time:2022/5/9 16:43
# @Author:Young
# @File:pandas叠加柱状图
import matplotlib.pyplot as plt
import pandas as pd
users = pd.read_excel("demo/test11.xlsx")
users["total"]=users["Oct"]+users["Nov"]+users["Dec"]
users.sort_values(by="total",inplace=True)
print(users)
# plot.barh就是水平翻转的意思
users.plot.barh(x="Name",y=["Oct","Nov","Dec"], stacked=True, title="User Behavior")
plt.tight_layout()
plt.show()