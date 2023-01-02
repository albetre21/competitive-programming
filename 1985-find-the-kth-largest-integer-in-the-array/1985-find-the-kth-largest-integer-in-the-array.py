class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        d=[int(x) for x in nums]
        d.sort(reverse=True)
            
        result=d[k-1]
        print(d)
        return str(result)
     