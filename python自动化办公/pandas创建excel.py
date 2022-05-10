# _*_coding:utf-8_*_
# @Time:2022/5/7 17:18
# @Author:Young
# @File:pandas创建excel

import pandas as pd

excel = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Yang", "yun", "hun"]})
df = excel.set_index("ID")
print(df)
df.to_excel("demo/1.xlsx")