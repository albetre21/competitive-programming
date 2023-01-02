class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        i=0
        end=len(nums)-1
        add_pair=0
        maximum=0
        while i<=end:
            add_pair=nums[i]+nums[end]
            maximum=max(maximum,add_pair)
            i+=1
            end-=1            
        return maximum