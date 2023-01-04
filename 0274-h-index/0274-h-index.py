class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        count = {}
        citations.sort()
        ans = 0
        for i in range(len(citations)):
            count[citations[i]] = len(citations) - i
            if( citations[i] >= count[citations[i]]):
                ans = max(ans, count[citations[i]])
        return ans