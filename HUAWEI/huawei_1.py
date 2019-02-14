#! /usr/bin/python
# coding:utf-8
# 空水瓶问题

while 1:
    try:
        empty = int(input())
        if empty:
            total = 0
            while empty >= 3:
                exchange = empty // 3
                empty = exchange + empty % 3
                total += exchange
            if empty == 2:
                total = total + 1
            print total
        else:
            break
    except:
        break
# 总结：用两个空水两瓶换一个，总数除以2即可

