```python
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s) == 0:
            return ""
        s = list(s)
        for i in range(0, n):
            temp = s[0]
            s.remove(s[0])
            s.append(temp)
        return "".join(s)
```
