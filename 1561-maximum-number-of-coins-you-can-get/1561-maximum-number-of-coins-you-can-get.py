class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles=sorted(piles)
        me=[piles[i] for i in range(int(len(piles)/3),len(piles),2)]
        add=sum(me)
        return add