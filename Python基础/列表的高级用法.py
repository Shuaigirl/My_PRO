# _*_coding:utf-8_*_
# @Time:2022/4/1 17:01
# @Author:Young
# @File:列表的高级用法
#列表的增删改查
#添加--------------------------
#append添加z在列表的最后添加一个对象或者数据
# food_list=['大鳄','五花肉']
# print(food_list)
# food_list.append('小鸡')
# print(food_list)

# char_list=['a','c','d']
# print(char_list)
# #insert(index,数据)其中index就是要插入的位置下标
# char_list.insert(1,'b')
# print(char_list)

#extend继承
# num_list=[1,2,3]
# num2_list=[4,5,6]
# num_list.extend(num2_list)
# print(num_list)

#修改-------------------------------
#通过下标来修改，下标从0开始
# city_list=['beijing','guanzhou','shenzheng','cahngan']
# print(city_list)
# city_list[2]='anquan'
# print(city_list)

#查找------------------------
#in 是判断某个元素是否在列表中
# food_list=['过把头','啥猪肉','东北鲁昂']
# food=input('请输入你的食物')
# if food in food_list:
#     print('在')
# else:
#     print('不在')

#not in 是判断某个元素是否在列表中
# ball_list = ['篮球','排球','足球']
# ball = input("请输入你的喜欢的球类：")
# if ball not in ball_list:
#     print('不在')
# else:
#     print('在')


#列表高级--删除
b_list=[1,2,3,4,5,6]
print(b_list)
#del 变量.[下标]根据下标删除
# del b_list[3]
# 变量.pop()删除最后一个数据
# b_list.pop()
#remove 根据元素的值来删除
b_list.remove(3)
print(b_list)

c_list=['河北','北京','大连'，]
