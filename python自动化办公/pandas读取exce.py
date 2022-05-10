# _*_coding:utf-8_*_
# @Time:2022/5/7 17:27
# @Author:Young
# @File:pandas读取exce
import pandas as pd

fp = pd.read_excel("demo/test.xlsx",header=None)
#读取excel文件的行列数:4行15列
print(fp.shape)
#读取excel列头,有时候列头是错位的，这时候我们就要设置header=第几行，从0开始，
#如果第一行没有数据，则不需要设置header,默认从有数据的行开始读取数据
#如果没有里列头，只有数据，那么我们可以设置header=none，然后手动设计列头
fp.columns = ["序列","下单日期","发货单位",	"发货人"	,"发货人电话","发货省","发货市","发货区/县",	"发货详细地址","商品","件数","包装","重量(kg)",	"体积(方)",	"运费"]
print(fp.columns)
fp.set_index("序列",inplace=True)
fp.to_excel("demo/test2.xlsx")
#z再次读取test2.xlsx后  再to_excel后 生成的test3.xlsx后 还是会自动生成序列，如果想这个不自动生成这个序列，则需要设置index_col=""