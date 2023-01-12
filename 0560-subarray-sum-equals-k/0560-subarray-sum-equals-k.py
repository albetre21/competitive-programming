class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    sol = 0
    prefix = 0
    count = collections.Counter({0: 1})

    for num in nums:
      prefix += num
      sol += count[prefix - k]
      count[prefix] += 1

    return sol