```python
# -*- coding:utf-8 -*-
import copy
class Solution:
    def multiply(self, A):
        # write code here
        size = len(A)
        B = [1]*size
        for i in range(0, size):
            temp = copy.copy(A)
            temp.remove(A[i])
            B[i] = 1
            for j in temp:
                B[i] *= j
        return B
```
