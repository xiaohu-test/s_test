#-*- coding = utf-8 -*-
#@Time : 2022/07/09 16:50
#@Author : 小胡同学
#@File : else.py
#@Software : PyCharm

# A = "你好"
# B = 1
# C = "好的"
#
# temp_a = ">>>%s(%d):%s" %(A,B,C)
# print(temp_a)

# def a():
#     pass
#
#
# def B():
#     pass


# for i in range

import time

def count_execution_time(func,*args,**kwargs):
    time1 = time.time()
    func(*args, **kwargs)
    time2 = time.time()
    print('执行时间', time2 - time1)


def func2():
    print('你好，世界')


if __name__ == '__main__':
    count_execution_time(func2)
