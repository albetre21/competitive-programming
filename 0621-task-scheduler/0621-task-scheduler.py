class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d={}
        for i in tasks:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        
        srtd = sorted(d.values(), reverse = True)
        
        max_value = srtd[0]
        i = 0
        counter = 0
        while i < len(srtd) and srtd[i] == max_value:
            counter +=1
            i +=1
        
            
        res = (max_value -1) * (n +1) + counter
        
        return max( len(tasks), res)
        