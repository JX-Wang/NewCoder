## Newcoder 练习题
Programming language: Python 2.7.x
### 剑指offer66题  
#### [汽水瓶](https://github.com/JX-Wang/NewCoder/tree/master/%E6%B1%BD%E6%B0%B4%E7%93%B6)
思路：每次将手中的水瓶对3进行取余，将取余后的空水瓶加上换来的水瓶再进行兑换，直到手中的水瓶数量小于2，等于2时+1  
思路：空水平数量/2，向下取整  
#### [孩子们的游戏](https://github.com/JX-Wang/NewCoder/tree/master/%E5%AD%A9%E5%AD%90%E4%BB%AC%E7%9A%84%E6%B8%B8%E6%88%8F)
思路：每次拿到小礼品的孩子的位置为 (上一个小孩子的位置+m-1)%(小孩总数)，依次循环，直到列表中只有一个元素，输出即可
#### [求1+2...+n](https://github.com/JX-Wang/NewCoder/tree/master/%E6%B1%821+2...+n)
思路：采用递归的形式进行求解
#### [第一个只出现一次的字符](https://github.com/JX-Wang/NewCoder/tree/master/%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E5%AD%97%E7%AC%A6)
思路：遍历字符串，若在该字符的前后都没有出现该字符，将该字符输出，遍历结束后若返回-1
#### [数组中只出现一次的字符](https://github.com/JX-Wang/NewCoder/tree/master/%E6%95%B0%E7%BB%84%E4%B8%AD%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E5%AD%97%E7%AC%A6)
思路：遍历数组，每次遍历时都新建一个没有当前字符的暂时数组，若当前字符在暂时数组中找不到与之相同的字符，将其添加至结果列表中，直到结果列表中的字符为2，返回
#### [斐波那契数列](https://github.com/JX-Wang/NewCoder/edit/master/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97/README.md)
思路：做法十分简单，a[n] = a[n-1] + a[n-2]
#### [数值的n次方](https://github.com/JX-Wang/NewCoder/tree/master/%E6%95%B0%E5%80%BC%E7%9A%84n%E6%AC%A1%E6%96%B9)
思路：调用python内置的 ** 进行幂运算
