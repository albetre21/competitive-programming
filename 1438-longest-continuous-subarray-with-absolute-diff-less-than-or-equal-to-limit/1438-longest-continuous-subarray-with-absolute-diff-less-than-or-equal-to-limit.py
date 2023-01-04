class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQueue = deque()
        minQueue = deque()
        result = 0;
        right = 0
        left = 0
        
        while(right < len(nums)):
            
            while(len(maxQueue) > 0 and nums[maxQueue[-1]] <= nums[right]):
                maxQueue.pop()
            maxQueue.append(right)
                
            while (len(minQueue) > 0 and nums[minQueue[-1]] >= nums[right]):
                minQueue.pop()
            minQueue.append(right)
            
            if(nums[maxQueue[0]] - nums[minQueue[0]] <= limit):
                result = max(result, right-left +1)
                right += 1
            
            else:
                left+=1
                if(left > minQueue[0]):
                    minQueue.popleft()
                if left > maxQueue[0]:
                    maxQueue.popleft()
                
                
            
        return result
        