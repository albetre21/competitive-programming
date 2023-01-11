class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    """
        Do not return anything, modify nums in-place instead.
        """
    n = len(nums)

    i = n - 2
    while i >= 0:
      if nums[i] < nums[i + 1]:
        break
      i -= 1

    if i >= 0:
      for j in range(n - 1, i, -1):
        if nums[j] > nums[i]:
          nums[i], nums[j] = nums[j], nums[i]
          break

    def reverse(nums: List[int], l: int, r: int) -> None:
      while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    reverse(nums, i + 1, len(nums) - 1)
        