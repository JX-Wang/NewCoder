```python
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
```
