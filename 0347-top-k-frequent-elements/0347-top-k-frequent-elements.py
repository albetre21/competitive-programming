class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr=Counter(nums)
        count=list(ctr.values())
        dic=list(dict.fromkeys(nums))
        res=dict(zip(dic,count))
        final=sorted(res.items(),key=lambda x:(x[1],x[0]),reverse=True);
        obj=[]
        ans=[]
        for i in final:
             obj.append(i[0])
        for i in range(k):
            ans.append(obj[i])
       
    
        return ans