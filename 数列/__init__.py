#! /usr/bin/python
# coding:utf-8

"""
题目描述

某种特殊的数列a1, a2, a3, ...的定义如下：a1 = 1, a2 = 2, ... , an = 2 * an − 1 + an - 2 (n > 2)。

给出任意一个正整数k，求该数列的第k项模以32767的结果是多少？
输入描述:

第1行是测试数据的组数n，后面跟着n行输入。每组测试数据占1行，包括一个正整数k (1 ≤ k < 1000000)。

输出描述:

n行，每行输出对应一个输入。输出应是一个非负整数。

示例1
输入
复制

2
1
8

输出
复制

1
408


"""
while 1:
    n = input()
    a = [1, 2]
    while n >= 1:
        try:
            k = input()
            if k > 2:
                for i in range(2, k):
                    temp = 2*a[i-1] + a[i-2]
                    a.append(temp)
                print a[1] % 32767
            elif k == 1:
                print a[0] % 32767
            else:
                print a[1] % 32767
            print a
        except Exception as e:
            break
        n -= 1