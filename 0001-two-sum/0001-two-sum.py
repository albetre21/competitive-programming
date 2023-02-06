class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], i]
            else:
                values[value] = i