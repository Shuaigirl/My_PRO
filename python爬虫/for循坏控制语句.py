# _*_coding:utf-8_*_
# @Time:2022/4/1 16:18
# @Author:Young
# @File:for循坏控制语句
#for循坏
#格式：  for  变量  in  要遍历的数据

# s='china'
# #i是字符串中一个又一个的字符变量
# for i in s:
#     print(i)

#range 方法 ：range(5)  range(1,5)  range(1,10,3)
#range 方法：range(5)  一个可以遍历的对象

# for  i in range(5):
# print(i)

#range(起始值,结束值)
#range 方法 ：  range(1,5)   0-4左闭右开区别
# for  i in range(1,5):
#  print(i)


#range(起始值,结束值,步长)
#range(1,10,3)
#
# for i in range(1,20,3):
#     print(i)



#应用场景  会爬取一个列表返回给我们
a_list=['zhou','yang','hao','hun','yin']
# for i in a_list:
#     print(i)
# print(len(a_list))
for i in range(len(a_list)):
    print(i)
