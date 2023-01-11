class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        zeroes = 0
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] == 0: zeroes += 1
            while zeroes > 1:
                if nums[l] == 0: zeroes -= 1
                l += 1
            res = max(res, r-l+1-zeroes)
        return res-1 if res == n else res
        