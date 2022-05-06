# _*_coding:utf-8_*_
# @Time:2022/4/21 18:09
# @Author:Young
# @File:获取ts_json节点
import json
import csv
ts = open("demo/ts.json", "rb")
client = open("demo/clinet.json", "rb")
#json字符串转换为dict
post_json = json.load(ts)
post_clinet = json.load(client)

'''
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
'''
# print(post_json, post_clinet)
# print('二级节点：------------------------------')
# for ts_list, clinet_list in zip(sorted(post_json['shipment']),sorted(post_clinet['shipment'])):
#     print(ts_list,'----',clinet_list)
# print('三级节点：------------------------------')
# for ts_key,clinet_key in zip(sorted(post_json['shipment']['to_address']),sorted(post_clinet['shipment']['to_address'])):
#     print(ts_key,'-----',clinet_key)
# print('三级节点值：------------------------------')
# for ts_value, clinet_value in zip(sorted(post_json['shipment']['to_address'].items()),sorted(post_clinet['shipment']['to_address'].items())):
#         print(ts_value, '-----', clinet_value)

'''
需要返回全部节点，并进行比较
'''
for i in post_json['shipment']:
    if i == 'parcel_number':
        post_json['shipment'][i] = 'parcel'
        break

#
# print('---------------------------------')



#
# for ts_list in post_json['shipment']:
#     for clinet_list in post_clinet['shipment']:
#          if ts_list == clinet_list:
#             print(ts_list)