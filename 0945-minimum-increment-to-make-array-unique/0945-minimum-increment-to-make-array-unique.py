class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        count = dict()
        ans =  0
        largest = 0
        for i in range(len(nums)):
            
            if(count.get(nums[i]) == None):
                count[nums[i]] = 1
            else:
                ans += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i -1]  + 1 
            count[nums[i]] = 1
                
            
        return ans