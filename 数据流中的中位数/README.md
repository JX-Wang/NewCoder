```python
# -*- coding:utf-8 -*-
class Solution:
    def Insert(self, num):
        # write code here
        self.temp = []
        self.ret = []
        for i in num:
            self.temp.append(float(i))
            self.GetMedian()
        return " ".join(self.ret)

    def GetMedian(self):
        # write code here
        temp = sorted(self.temp)
        if len(temp) == 1:
            self.ret.append(str(temp[0]))
        elif len(temp) == 2:
            self.ret.append(str((temp[0] + temp[1]) / 2))
        elif len(temp) % 2 == 0:
            locate = len(temp) / 2
            self.ret.append(str((temp[locate - 1] + temp[locate]) / 2))
        else:
            self.ret.append(str(temp[(len(temp) - 1) / 2]))


if __name__ == '__main__':
    print Solution().Insert([5, 2, 3, 4, 1, 6, 7, 0, 8])
```
