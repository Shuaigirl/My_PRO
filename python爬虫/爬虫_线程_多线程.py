# _*_coding:utf-8_*_
# @Time:2022/4/12 14:27
# @Author:Young
# @File:爬虫_进程_单多线程


# 什么是线程/进程？
# 进程是资源单位,每一个进程至少要有一个线程
# 线程是一个执行单位

#启动每一个程序默认都会有一个主线程
# def func():
#     for i in range(1, 1000):
#
#         print("func:", i)
#
# if __name__ == '__main__':
#     func()
#     # print("你好啊")
#     for i in range(2, 999):
#         print('main:', i)
# #上面的程序可以开出，一直是一根线执行，一个执行完了另一个继续执行，所以属于单线程


# 怎么执行多线程呢？
# 多线程  首先要导包：Thread 线程类


#  第一种方法：
from threading import Thread
# def func():
#     for i in range(1000):
#         print('这是函数中程序的线程：', i)

# if __name__ == '__main__':
#     # 创建线程并给线程安排任务
#     t = Thread(target=func)# 注意这个的func不用加()，不是调用func()函数
#     # 多线程状态为可以开始工作的状态，具体执行时间由CPU决定
#     t.start()
#     # 还有很多的线程
#     # t2=Threat(XXXX)
#     # t2.start()
#     for i in range(1000):
#         print('这是主程序的线程：', i)

#  第二种方法：
from threading import Thread

def func(name):
        for i in range(1000):
             print(name, i)

if __name__ == '__main__':
    t1 = Thread(target=func, args=('周杰伦',))
    t1.start()
    t2 = Thread(target=func, args=('林俊杰',))
    t2.start()






# # 第三种方法：继承Thread类
# class MyThread(Thread):
#     def run(self):  # 固定的  ->当线程被执行的时候,被执行的就是run()
#         for i in range(1000):
#             print("这是子线程：", i)
#
# if __name__ == '__main__':
#      t =MyThread()
# #  t.run()这样写就是方法的调用 ->单线程
#      t.start()
#      for i in range(1000):
#         print("这是主线程：", i)
