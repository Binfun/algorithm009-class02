class Solution:
    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        x = 1
        for i in range(1, n):
            xx = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    xx = max(dp[j], xx)
            dp[i] = xx + 1
            x = max(dp[i], x)
        return x
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
                #print(d)
        return len(d)