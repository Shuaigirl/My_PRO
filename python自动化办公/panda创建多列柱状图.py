# _*_coding:utf-8_*_
# @Time:2022/5/9 15:48
# @Author:Young
# @File:panda创建多列柱状图
import matplotlib.pyplot as plt
import pandas as pd

fp = pd.read_excel("demo/test9_2.xlsx")
fp.sort_values(by=2022, inplace=True, ascending=False)
print(fp)
fp.plot.bar(x="Field", y=[2021, 2022], color=["orange","red"])
plt.title("International Student by Field",fontsize=16,fontweight="bold",color="red")
plt.xlabel("Field_all",fontweight="bold")
plt.ylabel("Year_2021/2022",fontweight="bold")
ax = plt.gca()
ax.set_xticklabels(fp["Field"],rotation=45, ha="right")
fy = plt.gcf()
fy.subplots_adjust(left=0.2,bottom=0.42)
# plt.tight_layout()
plt.show()


# plt.bar(fp.Field,fp["2021","2022"],color=["orange","red"])
# plt.xticks(fp.Field,rotation=90)
# plt.xlabel("Field")
# plt.ylabel(["2021",["2022"]])
# plt.title("International Student by Field",fontsize=16)
# plt.tight_layout()
# plt.show()
