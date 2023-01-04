class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        k = k - 1
        pos = 0
        players = [player for player in range(1, n+1)]
        
        def findWinner(pos, k):
            if len(players)  == 1:
                return players[0]
            pos = (pos + k) % len(players)
            del players[pos]
    
            return findWinner(pos, k)
        return findWinner(pos, k)
        