# _*_coding:utf-8_*_
# @Time:2022/5/11 10:44
# @Author:Young
# @File:pandas链接SQLserver数据库
import pandas as pd
# 安装pyodbc的时候直接用pip3 install pyodbc   不用加国内源链接，加了反而不能安装成功
import pyodbc
# pip install pymysql  -i https://pypi.douban.com/simple
# pip install flask_sqlalchemy -i https://pypi.douban.com/simple
import sqlalchemy

# 两种方式链接数据库
connection = pyodbc.connect("DRIVER={SQL Server};SERVER=(local);DATABASE=AdventureWorks;USER=sa;PASSWORD=123456")
engine = sqlalchemy.create_engine("mssql+pyodbc://sa:123456@(local/AdventureWorks?driver=SQL+server)")
query = "select FirstName,LastName from Persion.Person"
query2 = "select count(FirstName) as Count from Person.Person where FirstName='Yang'"
df1 = pd.read_sql_query(query, connection)
df2 = pd.read_sql_query(query2, engine)
print(df1.head())
print(df2.head())

