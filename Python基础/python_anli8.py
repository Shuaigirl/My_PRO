# _*_coding:utf-8_*_
# @Time:2022/4/23 16:20
# @Author:Young
# @File:python_anli8

# 时间函数举例
def test():
    for i in range(3000):
        print(i)

if __name__ == '__main__':
    from timeit import timeit
    t = timeit('test()', 'from __main__ import test', number=1)
    print(t)

    import time
    print(time.ctime(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))


