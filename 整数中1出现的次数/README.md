```python
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        ret = 0
        for i in range(1, n+1):
            temp_str = str(i)
            for j in temp_str:
                if j == '1':
                    ret += 1
                else:pass
        return ret
```
