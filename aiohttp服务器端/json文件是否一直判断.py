# _*_coding:utf-8_*_
# @Time:2022/4/20 9:31
# @Author:Young
# @File:json文件是否一直判断
import json

# 如何判断两个json是否完全相等
f1 = open("demo/ts.json", "rb")
f2 = open("demo/clinet.json", "rb")
json1 = json.load(f1)
json2 = json.load(f2)
# print(json1)
# print(json2)
for json1_list, json2_list in zip(sorted(json1['shipment']), sorted(json2['shipment'])):
    print(json1_list,'---', json2_list)
    # if json1_list != json2_list:
    #     print(json1_list, json2_list)
    #     print('------------------------------')




    # elif str(json1[json1_list]) != (json2[json2_list]):
    #    print(json1[json1_list],json2[json2_list])


# for json1_list, json2_list in zip(json1, json2):
#     # print(json1_list)
#     # print(json2_list)
#     if json1_list != json2_list:
#         print(json1_list, json2_list)



