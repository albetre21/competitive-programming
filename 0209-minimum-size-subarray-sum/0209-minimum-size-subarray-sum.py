class Solution:
  def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    sol = math.inf
    summ = 0
    j = 0

    for i, num in enumerate(nums):
      summ += num
      while summ >= s:
        sol = min(sol, i - j + 1)
        summ -= nums[j]
        j += 1

    return sol if sol != math.inf else 0