class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFree = 1
        l,u = len(nums)-1,len(nums)-1
        while u >= maxFree:
            while l and k-(nums[u]-nums[l-1])>=0:
                k -= nums[u]-nums[l-1]
                l -= 1
            maxFree = max(maxFree,u-l+1) 
            k += (u-l) * (nums[u] - nums[u-1])
            u-=1
        return maxFree
        
        
        
        
        
        