```
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        ret = [0, 1]
        if n == 0 or n == 1:
            return n
        for i in range(2, n+1):
            ret.append(ret[len(ret)-2] + ret[len(ret)-1])
        return ret.pop()
```
