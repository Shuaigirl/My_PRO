# _*_coding:utf-8_*_
# @Time:2022/4/12 15:50
# @Author:Young
# @File:爬虫_线程池和进程池


# 线程池：一次性开辟一些线程，我们用户直接给线程池提交任务，线程任务的调度交给线程池来完成
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
def fn(name):
    for i in range(1000):
        print(name, i)

if __name__ == '__main__':
     # 创建线程池
      with ThreadPoolExecutor(50) as t:
          for i in range(100):
              t.submit(fn, name=f"线程{i}")
             # 等待线程池中的任务全部执行完毕，才能继续执行（守护）
      print('1243')
