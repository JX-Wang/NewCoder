#! /usr/bin/python
# coding:utf-8
# 去重与排序

while 1:
    try:
        numer = int(input())
        array = []
        for num in range(0, numer):
            temp = int(input())
            array.append(temp)
        array_1 = []
        for i in array:
            if not i in array_1:
                array_1.append(i)
        array_1.sort()
        for item in array_1:
            print item
    except:
        break

# 总结：使用列表数据结构，遍历去重后调用python内置sort函数排序

