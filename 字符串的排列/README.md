```python
# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        ret = []
        for i in itertools.permutations(ss, len(ss)):
            ret.append("".join(i))
        temp = list(set(ret))
        temp.sort(key=ret.index)
        return temp
```
