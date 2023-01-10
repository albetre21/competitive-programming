class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        start = 0
        end = len(people) - 1
        counter = 0
        
        people.sort()
        
        while end >= start:
            
            if start==end: 
                counter += 1
                break
                
            if people[start] <= limit - people[end]: 
                start += 1
                end -= 1
                counter += 1
                continue
            
            else: 
                end -= 1
                counter += 1
                
        return counter