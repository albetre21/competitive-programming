class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        n=len(nums) - 1
        while(l<=n):
            nums[l],nums[n] = nums[l]**2,nums[n]**2
            
            l+=1
            n -=1
            
        return sorted(nums)
        
        
        