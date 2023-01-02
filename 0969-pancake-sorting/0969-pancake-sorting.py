class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(k):
            l,r=0,k
            while l<r:
                arr[r],arr[l]=arr[l],arr[r]
                l+=1
                r-=1    
        res=[]
        index=len(arr)
        while index>0:
            if arr[index-1]!=index and index>0:
                k=arr.index(index)+1
                res.append(k)
                flip(arr.index(index))    
                k=index
                res.append(k)
                flip(index-1)        
            index-=1
        return res