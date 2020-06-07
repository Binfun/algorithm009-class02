class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def __dfs(idx, res, pre, nums):
            if not idx:
                if pre[:] not in res:
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

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:

                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if size == 0:
            return []

        nums.sort()

        used = [False] * len(nums)
        res = []
        dfs(nums, size, 0, [], used, res)
        return res

