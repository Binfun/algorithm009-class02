# 33. 搜索旋转排序数组 解题思路
题目： https://leetcode-cn.com/problems/search-in-rotated-sorted-array/submissions/

## 两种解法
1. 找到中间的旋转的那个点，那个点就是对应数组的最小值，从而知道了该数组实际上的最小值最大值。使用二分查找找到中间的那个点，再基于旋转点进行二分查找target.
2. 直接进行二分查找。通过比较数组最左边的值（nums）和mid的值，来定位当前mid是在旋转点前面还是后面。不断地二分查找并且不断地判断。

## 第一种

代码思路如下

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        l = 0
        r = length - 1
        while l < r:
            mid = (l + r) // 2
            if (nums[mid] > nums[r]):
                l = mid + 1
            else:
                r = mid
        # l 和 r 最终会在最小值的地方相等,从而退出while l < r循环
        m = l
        if m == 0: # 如果没有旋转点那么进行正常的二叉搜索
            r = length - 1
        else:
            if nums[0] <= target and target <= nums[m - 1]:
                l = 0
                r = m - 1
            elif nums[m] <= target and target <= nums[length - 1]:
                l = m
                r = length - 1
            else:
                return -1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
```

先通过二分查找找到旋转点，再判断想要查找的值是旋转点前面的区域还是旋转点后面的区域，再在那个区域里面进行二分查找，如下：

a1 a2 a3 a4 b5(旋转点) b6 b7 b8

a1-a4 是一个区域，b5-b8是另一个区域。

当然以上代码为了表达思路，显得比较冗余，参考以下代码会比较简洁
https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution

使用一个%就可以少写这么多的判断条件，真是妙啊！
```
            int mid=(lo+hi)/2;
            int realmid=(mid+rot)%n;
```

## 第二种

在第一种的解法当中我们知道了有旋转点：
a1 a2 a3 a4 b5(旋转点) b6 b7 b8
51 62 73 84 11         22 33 44 

是存在以上a区域和b区域的区别的，其实我们任何时候都是知道，（ l + r ) /2的这个mid是属于a区域还是属于b区域的。
比如nums[mid]的值是小于a1的话肯定是属于b区域，大于a1的话肯定就是a区域

### 寻找可控范围
如果当前mid的属于a区域的，那么a1 到 mid就是属于我们的可控范围，如果target的值大于等于nums[a1]并且小于nums[mid]，我们就把mid往a1(左边)靠。反之则把mid往b8方向靠。

同理，如果当前mid的属于b区域的，那么mid 到 b8 就是属于我们的可控范围，如果target的值大于nums[mid]并且小于等于nums[b8]，我们就把mid往b8(右边)靠。反之则把mid往a1方向靠。

可以得到以下代码：
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        x = r = len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[x]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
```
leetcode上著名光头哥的代码：
https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
其实和以上代码的根本逻辑是一样的，只不过是把上述代码中的三个if判断（if nums[0] <= nums[mid]）放在了一个表达式里，妙啊！
```
        double num = (nums[mid] < nums[0]) == (target < nums[0])
                   ? nums[mid]
                   : target < nums[0] ? -INFINITY : INFINITY;
```

## 总结
以上两种方法，第一种是做了两次O(logn)的二分查找，第二种方法是在一次二分查找中做了两次的条件判断。本质上没有区别。运行速度几乎相同都是：

执行结果：
通过
显示详情
执行用时 :
44 ms
, 在所有 Python3 提交中击败了48.61%的用户
内存消耗 :
13.8 MB, 在所有 Python3 提交中击败了7.69%的用户