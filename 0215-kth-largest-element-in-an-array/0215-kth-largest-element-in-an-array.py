class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        out=sorted(nums, reverse=True)
        return out[k-1]
        
        