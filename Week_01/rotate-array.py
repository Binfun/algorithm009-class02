class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        s = n = 0
        prev = nums[n]
        for i in range(l):
            n = (n + k) % l
            nums[n], prev = prev, nums[n]
            if n == s:
                s = n = (n + 1) % l
                prev = nums[n]
