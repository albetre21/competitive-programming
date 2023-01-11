class Solution:
  def maxScore(self, cardPoints: List[int], k: int) -> int:
    n = len(cardPoints)
    summ = sum(cardPoints)
    windowSum = sum(cardPoints[:n - k])
    sol= summ - windowSum

    for i in range(k):
      windowSum -= cardPoints[i]
      windowSum += cardPoints[i + n - k]
      sol = max(sol, summ - windowSum)

    return sol