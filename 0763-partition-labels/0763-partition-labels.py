class Solution:
  def partitionLabels(self, S: str) -> List[int]:
    A = []
    letterToRightmostIndex = {c: i for i, c in enumerate(S)}

    l = 0
    r = 0

    for i, c in enumerate(S):
      r = max(r, letterToRightmostIndex[c])
      if i == r:
        A.append(r - l + 1)
        l = r + 1

    return A