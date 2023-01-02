class Solution:
    def isValid(self, s: str) -> bool:
        bracket={")":"(","}":"{","]":"["}
        val=[]
        for i in s:
            if not val:
                val.append(i)
            else:
                val.pop() if bracket.get(i)==val[-1] else val.append(i)
             
        return(False, True)[not val]