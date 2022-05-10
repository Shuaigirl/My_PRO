# _*_coding:utf-8_*_
# @Time:2022/5/9 11:24
# @Author:Young
# @File:pandas获取数据区域填充数字
import pandas as pd
from datetime import date,timedelta
fp =pd.read_excel("demo/test2.xlsx",skiprows=2,usecols="B:E",index_col=None,dtype={"ID":str,"Instore":str,"Date":str})
start =date(2022,1,1)
def add_month(d,md):
    yd=md//12
    m=d.month+md%12
    if m !=12:
        yd+=m//12
        m=m%12
    return date(d.year+yd,m,d.day)

for i in fp.index:
    fp["ID"].at[i] = i+1
    fp["Instore"].at[i] = "yes" if i % 2 == 0 else "no"
    # fp["Date"].at[i] =start+timedelta(days=i) #按天数递增
    # fp["Date"].at[i] = date(start.year+i,start.month,start.day)#按年份递增
    fp["Date"].at[i] = add_month(start,i)#按月份递增
fp.set_index("ID", inplace=True)
fp.to_excel("demo/test3.xlsx")
print("Done")

