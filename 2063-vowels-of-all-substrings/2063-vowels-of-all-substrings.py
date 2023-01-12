class Solution:
  def countVowels(self, word: str) -> int:
    dp = [0] * (len(word) + 1)

    for i, c in enumerate(word):
      dp[i + 1] = dp[i] + (c in 'aeiou') * (i + 1)

    return sum(dp)