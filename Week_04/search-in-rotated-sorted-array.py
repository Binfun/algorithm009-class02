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
