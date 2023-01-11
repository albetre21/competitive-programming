class Solution:
  def maxVowels(self, s: str, k: int) -> int:
    sol = 0
    maxi = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for i, c in enumerate(s):
      if c in vowels:
        maxi += 1
      if i >= k and s[i - k] in vowels:
        maxi -= 1
      sol = max(sol, maxi)

    return sol