class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        amount = len(nums)
        while amount > k:
            heapq.heappop(nums)
            amount -= 1
        return nums[0]
        