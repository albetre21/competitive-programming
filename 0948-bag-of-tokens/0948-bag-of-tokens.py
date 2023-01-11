class Solution:
  def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
    c = 0
    score = 0
    q = collections.deque(sorted(tokens))

    while q and (power >= q[0] or score):
      while q and power >= q[0]:
        # Play the smallest face up
        power -= q.popleft()
        score += 1
      c = max(c, score)
      if q and score:
        # Play the largest face down
        power += q.pop()
        score -= 1

    return c