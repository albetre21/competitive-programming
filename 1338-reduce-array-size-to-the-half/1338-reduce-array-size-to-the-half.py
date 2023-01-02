class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ans=0      
        count=defaultdict(int)
        
        l=(len(arr)-1)//2      
        for i in arr:
            count[i]+=1            
        occ=0        
        for x in sorted(count.values(),reverse=True):            
            if occ>l:
                return ans
            else:
                occ+=x
                ans+=1
        return ans