class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        current_max,ans="",""
        nums=[str(i) for i in nums]
        while nums:
            for i in nums:
                if not current_max:
                    current_max=i
                else:    
                    if i+current_max>current_max+i:
                        current_max=i
            ans+=current_max
            nums.remove(current_max)
            current_max=""
        return ans if not ans.startswith("0") else "0"
        