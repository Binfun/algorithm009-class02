## 编辑距离题解
https://leetcode-cn.com/problems/edit-distance/solution/ji-yi-di-gui-ji-bai-liao-90de-yong-hu-dong-tai-gui/
### 记忆化递归
例如比较字符串horse和rose：

h o r s e五个字符分别用w1[0] w1[1] w1[2] w1[3] w1[4] 表示。

r o s e 四个字符分别用w2[0] w2[1] w2[2] w2[3] 表示。

那么我们现在的目标就是把horse变成rose, horse是源单词, rose是目标单词。

现在先比较w1[0]和w2[0]即h和r，发现不相等，那么我们现在有三种选择：
1. 修改当前字符。我把h修改成r, 然后再继续比较w1[1]和w2[1]。
2. 删除当前字符。既然h和r不相等，那么h我不要了我删掉，然后再继续比较w1[1]和w2[0]
3. 在当前字符前面再插入一个字符。即我在h前面插入r，然后再继续比较w1[0]和w2[1]

以上三种分叉就是当字符不相等时递归中的三个调用。

再例如当比较到w1[1]和w2[1]的时候，都是o，字符是相等的，这个我们肯定是既不需要插入也不需要删除，也不需要修改，再继续比较w1[2]和w2[2]就行了。

基于以上思路，记忆化递归代码如下：
```
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = [ [-1 for j in range(len(word2) + 1)] for i in range(len(word1) + 1) ]
        def sub(i1: int, i2: int) -> int:
            if i1 == len(word1):
                return len(word2) - i2
            elif i2 == len(word2):
                return len(word1) - i1
            if word1[i1] == word2[i2]:
                if m[i1 + 1][i2 + 1] == -1:
                    m[i1 + 1][i2 + 1] = sub(i1 + 1, i2 + 1)
                return m[i1 + 1][i2 + 1]
            else:
                if m[i1][i2 + 1] == -1:
                    m[i1][i2 + 1] = sub(i1, i2 + 1)
                if m[i1 + 1][i2] == -1:
                    m[i1 + 1][i2] = sub(i1 + 1, i2)
                if m[i1 + 1][i2 + 1] == -1:
                    m[i1 + 1][i2 + 1] = sub(i1 + 1, i2 + 1)
                return min(m[i1][i2 + 1], m[i1 + 1][i2], m[i1 + 1][i2 + 1]) + 1
        return sub(0, 0)
```

### 动态规划
通过上面的记忆化递归，我们可以感受到那个“隐形”的表格，现在我们让这个表格浮出水面。

\ | r | o | s | e
--- | --- | --- | --- | ---
h| 1| 2| 3| 4
o| 2| 1| 2| ***3***
r| 2| 2| 2| 3
s| 3| 3| 2| 3
e| 4| 4| 3| 2

我们现在的目标依然是要把 horse 变成 rose。 我们会在代码中创建一个len("horse")行、len("rose")列的数组m。

每个格子代表的数字是什么意思呢？举个例子比如数组m[1][3] (horse的o那一行，rose的e那一列)的值3，就是上表格中加粗斜体的3，其代表的意思就是字符串ho转换成字符串rose的最小操作数。

同理可得：
m[0][2] 代表h转换成ros的最小操作数
m[0][3] 代表h转换成rose的最小操作数
m[1][2] 代表ho转换成ros的最小操作数

m[0][2] ( h->ros) m[0][3] (h->rose)
m[1][2] (ho->ros) m[1][3] (ho->rose)

以上我们可以看出想要推演出ho->rose的最小操作数有几个途径可以走：
1. 先把h转换成ros （m[0][2]的值），再把o替换成e（替换的操作会让操作数加一）
2. 先把h转换成rose（m[0][3]的值），再把o删除掉 （任何情况下，删除的操作会让操作数加一）
3. 先把ho转换成ros（m[1][2]的值），再插入e （任何情况下，插入的操作会让操作数加一）

以上当ho的最后一个字母和rose的最后一个字母e不相等的情况下，取以上三条路径中最小的一条即可：
```
m[i][j] = min(m[i - 1][j - 1], m[i - 1][j], m[i][j - 1]) + 1
```
m[i-1][j-1] m[i-1][j]
m[i][j-1]     m[i][j]

那么如果horse的第i个字母和rose的第j个字母相等的情况下，我们应该取哪个路径？

我们知道删除horse的第i个字母，或者插入rose的第j个字母，这两个操作都是不需要比较第i和第j个字母的。

那么：
```
                if word1[i] == word2[j]:
                    m[i][j] = m[i - 1][j - 1]
```
如何证明字母相等的情况下m[i][j] = m[i - 1][j - 1]就是最短路径？

我们从字符串长短就可以推算出 |m[i-1][j-1] - m[i-1][j]| <= 1 以及 |m[i-1][j-1] - m[i][j-1]| <= 1 以上的绝对值一定是小于等于1

那么可得：
m[i][j] = m[i - 1][j - 1] <= m[i-1][j] + 1
以及：
m[i][j] = m[i - 1][j - 1] <= m[i][j-1] + 1

代码如下，我对表格的第0行和第0列做了特殊处理：

```
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2) == 0:
            return len(word1)
        elif len(word1) == 0:
            return len(word2)
        m = [ [0 for i in range(len(word2))] for j in range(len(word1))]
        p = 0
        for j in range(len(word2)): #初始化第0行
            if word1[0] == word2[j]:
                p = 1
            m[0][j] = j + 1 - p
        p = 0
        for i in range(0, len(word1)): #初始化第0列
            if word1[i] == word2[0]:
                p = 1
            m[i][0] = i + 1 - p

        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                if word1[i] == word2[j]:
                    m[i][j] = m[i - 1][j - 1]
                else:
                    m[i][j] = min(m[i - 1][j - 1], m[i - 1][j], m[i][j - 1]) + 1
        return m[-1][-1]
```


