## 最长公共子序列
[https://leetcode-cn.com/problems/longest-common-subsequence/](https://leetcode-cn.com/problems/longest-common-subsequence/)

两种解决方法：自顶向下的暴力递归加备忘数组 以及 自底向上的备忘数组的推演——动态规划，因为如果单纯暴力递归的话会超时，所以需要加上备忘数组。

再得到这样记忆化搜索的备忘数组之后会发现，动态规划就是在推演这个备忘数组。他们是自顶向下和自底向上的区别。

### 自顶向下的暴力递归加备忘数组
```
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        def dp(i, j):
            k, h = i + 1, j + 1
            if i == -1 or j == -1:
                a[k][h] = 0
                return 0
            if text1[i] == text2[j]:
                if a[k][h] == -1:
                    a[k - 1][h - 1] = dp(i - 1, j - 1)
                    a[k][h] = a[k - 1][h - 1] + 1
            else:
                if a[k-1][h] == -1: a[k-1][h] = dp(i-1, j)
                if a[k][h-1] == -1: a[k][h-1] = dp(i, j-1)
                a[k][h] = max(a[k-1][h], a[k][h-1])
            return a[k][h]
        dp(len(text1)-1, len(text2)-1)
        #print(a)
        return a[-1][-1]
```

此时如果输入参数“cbaa”和"acb"的话，并将代码中的a打印出来：
\ | null | a | c | b
--- | --- | --- | --- | ---
null | -1 | 0 | -1 | -1
c|0| 0| 1| -1
b|0| 0| 1| 2
a|0| 1| 1| 2
a|-1| 1| 1| 2

## 自底向上的备忘数组的推演——动态规划
```
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        #print(dp)
        return dp[-1][-1]
```
此时如果输入参数“cbaa”和"acb"的话，并将dp打印出来：

\ | null | a | c | b
--- | --- | --- | --- | ---
null | 0 | 0 | 0 | 0
c|0| 0| 1| 1
b|0| 0| 1| 2
a|0| 1| 1| 2
a|0| 1| 1| 2

## 小结
以上的两个表格就是从不同的角度看待同一个东西。

