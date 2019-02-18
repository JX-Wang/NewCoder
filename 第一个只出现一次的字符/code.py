```
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        size = len(s)
        for i in range(0, size):
            if s[i] not in s[i+1:] and s[i] not in s[:i]:
                return i
        return -1
```
