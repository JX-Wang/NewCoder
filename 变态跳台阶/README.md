```python
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1 or number == 2:
            return number
        temp = [1, 2]
        for i in range(2, number):
            n = 0
            for j in temp:
                n += j
            temp.append(n + 1)
        return temp.pop()
```
