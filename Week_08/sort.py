from typing import List

class Solution:
    def bubble_sort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1): # just need to bubble n-1 times if there are n nums
            for j in range(1, len(nums) - i): # just need to compare n-i-1 times
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        return nums

    def select_sort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            k = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[k]:
                    k = j
            nums[k], nums[i] = nums[i], nums[k]
        return nums

    def insert_sort(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        return nums

    def quick_sort(self, nums: List[int]) -> List[int]:
        def get_pivot(n: List[int], l: int, r: int):
            c = l
            for i in range(l, r):
                if (n[i] < n[r]):
                    n[i], n[c] = n[c], n[i]
                    c += 1
            n[c], n[r] = n[r], n[c]
            #print(n)
            return c
        def sub_quick(n: List[int], l: int, r: int):
            if l >= r:
                return
            #print("l: " + str(l) + " and r: " + str(r))
            pivot = get_pivot(n, l, r)
            sub_quick(n, l, pivot - 1)
            sub_quick(n, pivot + 1, r)
        sub_quick(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums: List[int]) -> List[int]:
        def sub_merge(n: List[int], l: int, r: int):
            if l >= r: return
            m = (l + r) >> 1
            sub_merge(n, l, m)
            sub_merge(n, m + 1, r)
            t, i, j = [], l, m + 1
            while(i <= m and j <= r):
                if n[i] < n[j]:
                    t.append(n[i])
                    i += 1
                else:
                    t.append(n[j])
                    j += 1
            while(i <= m):
                t.append(n[i])
                i += 1
            while(j <= r):
                t.append(n[j])
                j += 1
            for k in range(len(t)):
                n[k + l] = t[k]
        sub_merge(nums, 0, len(nums) - 1)
        return nums