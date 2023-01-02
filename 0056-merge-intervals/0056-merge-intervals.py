class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        ret = []
        for i in intervals:
            newInterval = i           
            if ret:
                if ret[-1][1] >= i[0]:                     
                    newInterval = ret.pop()
                    if i[1] > newInterval[1]:
                        newInterval[1] = i[1]      
            ret.append(newInterval)
        return ret
        