## Newcoder 练习题
Programming language: Python 2.7.x
### 剑指offer66题  
#### [孩子们的游戏](https://github.com/JX-Wang/NewCoder/tree/master/%E5%AD%A9%E5%AD%90%E4%BB%AC%E7%9A%84%E6%B8%B8%E6%88%8F)
思路：每次拿到小礼品的孩子的位置为 (上一个小孩子的位置+m-1)%(小孩总数)，依次循环，直到列表中只有一个元素，输出即可
#### [求1+2...+n](https://github.com/JX-Wang/NewCoder/tree/master/%E6%B1%821+2...+n)
思路：采用递归的形式进行求解
#### [第一个只出现一次的字符](https://github.com/JX-Wang/NewCoder/tree/master/%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E5%AD%97%E7%AC%A6)
思路：遍历字符串，若在该字符的前后都没有出现该字符，将该字符输出，遍历结束后若返回-1
#### [数组中只出现一次的字符](https://github.com/JX-Wang/NewCoder/tree/master/%E6%95%B0%E7%BB%84%E4%B8%AD%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E5%AD%97%E7%AC%A6)
思路：遍历数组，每次遍历时都新建一个没有当前字符的暂时数组，若当前字符在暂时数组中找不到与之相同的字符，将其添加至结果列表中，直到结果列表中的字符为2
#### [斐波那契数列](https://github.com/JX-Wang/NewCoder/edit/master/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97/README.md)
思路：做法十分简单，a[n] = a[n-1] + a[n-2]
#### [数值的n次方](https://github.com/JX-Wang/NewCoder/tree/master/%E6%95%B0%E5%80%BC%E7%9A%84n%E6%AC%A1%E6%96%B9)
思路：调用python内置的 ** 进行幂运算
#### [跳台阶](https://github.com/JX-Wang/NewCoder/tree/master/%E8%B7%B3%E5%8F%B0%E9%98%B6)
思路：与斐波那契数列做法相似
#### [变态跳台阶](https://github.com/JX-Wang/NewCoder/tree/master/%E5%8F%98%E6%80%81%E8%B7%B3%E5%8F%B0%E9%98%B6)
思路：a[n] = a[0] + ... + a[n-1]
#### [替换空格](https://github.com/JX-Wang/NewCoder/tree/master/替换空格)
思路：使用python内置的对于str的replace()方法
#### [整数中1出现的次数](https://github.com/JX-Wang/NewCoder/tree/master/%E6%95%B4%E6%95%B0%E4%B8%AD1%E5%87%BA%E7%8E%B0%E7%9A%84%E6%AC%A1%E6%95%B0)
思路：将整数变为字符串，遍历字符串
#### [构建乘积数组](https://github.com/JX-Wang/NewCoder/tree/master/%E6%9E%84%E5%BB%BA%E4%B9%98%E7%A7%AF%E6%95%B0%E7%BB%84)
思路：对于B中的每个元素，构建一个去掉A中对应该下标元素的数组temp，将temp中的所有元素进行乘积后赋值给B中对应位置的元素即可
#### [翻转单词序列](https://github.com/JX-Wang/NewCoder/tree/master/%E5%8F%8D%E8%BD%AC%E5%8D%95%E8%AF%8D%E5%BA%8F%E5%88%97)
思路：调用python内置的reverse()方法进行翻转  
#### [数据流中的中位数](https://github.com/JX-Wang/NewCoder/tree/master/%E6%95%B0%E6%8D%AE%E6%B5%81%E4%B8%AD%E7%9A%84%E4%B8%AD%E4%BD%8D%E6%95%B0)
思路：遍历原始列表，依次向temp列表中添加元素，再调用sorted()方法对temp列表进行排序再进行中位数的计算（代码可以得到正确结果，但是再newcoder这里通过不了）





### 其他练习题
#### [汽水瓶](https://github.com/JX-Wang/NewCoder/tree/master/%E6%B1%BD%E6%B0%B4%E7%93%B6)
思路：每次将手中的水瓶对3进行取余，将取余后的空水瓶加上换来的水瓶再进行兑换，直到手中的水瓶数量小于2，等于2时+1  
思路：空水平数量/2，向下取整  
#### [大整数相乘](https://github.com/JX-Wang/NewCoder/tree/master/%E5%A4%A7%E6%95%B4%E6%95%B0%E7%9B%B8%E4%B9%98)
思路：python支持大整数
#### [最大乘积](https://github.com/JX-Wang/NewCoder/tree/master/%E6%9C%80%E5%A4%A7%E4%B9%98%E7%A7%AF)
思路：排序后将首位四个数进行三个为组进行乘积操作，输出数值最大的数（该方法可以输出正确结果，但是nowcoder这里通不过）
#### [去重排序](https://github.com/JX-Wang/NewCoder/tree/master/%E5%8E%BB%E9%87%8D%E6%8E%92%E5%BA%8F)
思路：新建一个列表，每次从原始列表中向新建列表中添加元素时先检测是否有相同的元素，有则不添加，没有则反之，添加完后调用sort()进行排序
