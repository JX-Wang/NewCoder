```python
# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1:return -1
        temp = []
        for i in range(0, n):
            temp .append(i)
        self.t = 0
        for j in range(0, n - 1):
            self.t = (m-1+self.t)%len(temp)
            temp.remove(temp[self.t])
        return temp[0]
```
