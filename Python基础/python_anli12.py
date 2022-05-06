# _*_coding:utf-8_*_
# @Time:2022/4/25 11:02
# @Author:Young
# @File:python_anli12
# 题目：暂停一秒输出;程序分析：使用 time 模块的 sleep() 函数。
# import time
# l = [1, 2, 3, 4]
# print(len(l))
# for i in range(len(l)):
#     print(l[i])
#     time.sleep(1)  # 暂停一秒输出
#

#题目：暂停一秒输出，并格式化当前时间。
# import time,datetime
# time.sleep(3)
# TIME = datetime.datetime.now()
# print(TIME)
# print(TIME.strftime("%Y/%m/%d %H:%M:%S"))

# 输出指定格式的日期。
import datetime

if __name__ == '__main__':
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%d/%m/%Y'))

    # 创建日期对象
    miyazakiBirthDate = datetime.date(1941, 1, 5)

    print(miyazakiBirthDate.strftime('%d/%m/%Y'))

    # 日期算术运算
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)

    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

    # 日期替换
    miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)

    print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))