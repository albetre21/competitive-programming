class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        tempStack = []
        
        tempMap = [[pos, spe] for pos, spe in zip(position, speed)]
        
        for pos, spe in sorted(tempMap, reverse=True):
            
            tempStack.append((target - pos)/ spe)
            if(len(tempStack) > 1 and  tempStack[-1] <= tempStack[-2] ):
                tempStack.pop()
        
        return len(tempStack)