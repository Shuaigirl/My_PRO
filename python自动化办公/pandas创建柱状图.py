# _*_coding:utf-8_*_
# @Time:2022/5/9 15:23
# @Author:Young
# @File:pandas创建柱状图
import pandas
import matplotlib.pyplot as plt
import pandas as pd

fp = pd.read_excel("demo/test9.xlsx")
fp.sort_values(by="Number",inplace=True,ascending=False)
# 这是第一种方法绘制柱状图
# fp.plot.bar(x="Field",y="Number",color="orange",title="International Student by Field")
# plt.show()
# 这是第二种方法绘制柱状图
plt.bar(fp.Field,fp.Number,color="orange")
plt.xticks(fp.Field,rotation=90)
plt.xlabel("Field")
plt.ylabel("Number")
plt.title("International Student by Field",fontsize=16)
plt.tight_layout()
plt.show()


