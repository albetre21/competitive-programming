class Solution:
  def threeSumMulti(self, A: List[int], target: int) -> int:
    kMod = 1_000_000_007
    sol = 0
    count = collections.Counter(A)

    for i, x in count.items():
      for j, y in count.items():
        k = target - i - j
        if k not in count:
          continue
        if i == j and j == k:
          sol = (sol + x * (x - 1) * (x - 2) // 6) % kMod
        elif i == j and j != k:
          sol = (sol + x * (x - 1) // 2 * count[k]) % kMod
        elif i < j and j < k:
          sol = (sol + x * y * count[k]) % kMod

    return sol % kMod