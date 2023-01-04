class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater=[]
        dic={}
        
        for i in range(len(nums2)):
            j=i+1
            while j<len(nums2) and nums2[i]>nums2[j]:
                j=j+1
            if j==len(nums2):
                dic[nums2[i]]=-1
            else:
                dic[nums2[i]]=nums2[j]
        for i in nums1:
            if(i in dic):
                nextGreater.append(dic[i])
            else:
                nextGreater.append(-1)
        return nextGreater