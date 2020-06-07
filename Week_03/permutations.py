class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def __dfs(idx, res, pre, nums):
            if not idx:
                res.append(pre[:])
                return
            temp = idx.copy()
            for i in temp:
                pre.append(nums[i])
                idx.remove(i)
                __dfs(idx, res, pre, nums)
                idx.append(i)
                pre.pop()

        idx = []
        res = []
        pre = []
        for i in range(len(nums)):
            idx.append(i)
        __dfs(idx, res, pre, nums)
        return res
        
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, state, res):
            if depth == size:
                res.append(path)
                return

            for i in range(size):
                if ((state >> i) & 1) == 0:
                    dfs(nums, size, depth + 1, path + [nums[i]], state ^ (1 << i), res)

        size = len(nums)
        if size == 0:
            return []

        state = 0
        res = []
        dfs(nums, size, 0, [], state, res)
        return res
