# _*_coding:utf-8_*_
# @Time:2022/4/27 14:19
# @Author:Young
# @File:python_pandas读取pdf文件
import pdfplumber
import pandas as pd
import csv
'''
.extract_text() 用来提页面中的文本，将页面的所有字符对象整理为的那个字符串
.extract_words() 返回的是所有的单词及其相关信息
.extract_tables() 提取页面的表格
.to_image() 用于可视化调试时，返回PageImage类的一个实例

'''
with pdfplumber.open("demo/test.pdf") as pdf:
    page = pdf.pages[0]   # 第一页的信息
    table = page.extract_tables() #得到一个list列表数据
    for t in table:
        # 得到的table是嵌套list类型，转化成DataFrame
       df = pd.DataFrame(t[1:], columns=t[0])
       # fwrite = csv.writer(open('demo/test.csv', 'w', encoding='utf-8'))
       # fwrite.writerow(df)
       print(df)
       # df.to_csv('demo/test.csv', encoding='utf-8')
