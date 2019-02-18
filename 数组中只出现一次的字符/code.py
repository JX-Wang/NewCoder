```
# -*- coding:utf-8 -*-
import copy

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        count = 0
        size = len(array)
        ret = []
        while count != 2:
            for i in range(0, size):
                temp = copy.copy(array)
                num = array[i]
                temp.remove(array[i])
                if num not in temp:
                    count += 1
                    ret.append(num)
                else:pass
        return ret
```
