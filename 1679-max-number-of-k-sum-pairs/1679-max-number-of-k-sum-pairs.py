import math 
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts=defaultdict(int)
        res_value=0
        for i in nums:
            if counts[i]>0:
                counts[i]-=1
                res_value+=1
            else:
                counts[k-i]+=1
        
        return res_value
    
