# _*_coding:utf-8_*_
# @Time:2022/5/10 17:12
# @Author:Young
# @File:pandas筛选无效区域数据
import pandas as pd

def score_validation(row):
    # 第一种方法
    # try :
    #     assert 0<=row.Score<=100
    # except:
    #     print(f"#{row.ID}\t{row.Name} has an invalid score:{row.Score}")
    # 第二种方法
    if not 0 <= row.Score <= 100:
        print(f"#{row.ID}\t{row.Name} has an invalid score:{row.Score}")

students = pd.read_excel("demo/test17.xlsx")
students.apply(score_validation,axis=1)
# print(students)