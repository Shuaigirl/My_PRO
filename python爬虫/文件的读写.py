# _*_coding:utf-8_*_
# @Time:2022/4/6 15:22
# @Author:Young
# @File:文件的读写
#创建一个文件
#open(文件的路径,模式)
# 模式：w读写
#      r可读
# fp=open('text.txt','w')
# fp.write('hello world')

# #文件夹是不可以创建的  暂时需要手动添加
# fp=open('demo/text.txt','w')
#  fp.write('hello world')


#w文件的关闭

# fp=open('demo/text2.txt','w')
#
# fp.write('remember to close  this chengxu \n '*10)
#
# fp.close()


#如果再次运行这段代码是打印5次还是后面的10次？
#r如果文件存在，会先翻盖原来的数据，然后在写入
#我想在每一次执行之后都需要追加数据
#如果模式变为a  那么就会执行追加的操作

# fp=open('demo/text.txt','a')
# fp.write('I love  you \n'*5)
# fp.close()


#读取数据
fp = open('demo/text.txt' , 'r')
#默认情况下，read是一字节一字节的读  效率比较低
# content = fp.read()
# print(content)

#readline是一行一行的读取，但是只读取一行
# content=fp.readline()
# print(content)
# fp.close()

#readlines可以按照行来读取，但是会将所有的数据都渠道并以列表的形式返回
content = fp.readlines()
print(content)
fp.close()


