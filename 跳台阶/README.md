```python
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1 or number ==2:
            return number
        temp = [1, 2]
        for i in range(2, number):
            temp.append(temp[i-2] + temp[i-1])
        return temp.pop()
```
