class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        minHeigh = 0
        maxArea = 0
        while l < r:
            minHeight = min(height[l],height[r])
            maxArea = max(maxArea,minHeight * ( r - l))
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
                
        return maxArea  