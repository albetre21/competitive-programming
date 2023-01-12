class Solution:
  def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    sol = []
    xors = [0] * (len(arr) + 1)

    for i, a in enumerate(arr):
      xors[i + 1] ^= xors[i] ^ a

    for l, r in queries:
      sol.append(xors[l] ^ xors[r + 1])

    return sol