class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            
            while len(stack) > 0 and int(num[i]) < int(stack[-1]) and k > 0 :
                if(num[i] == 0):
                    stack.pop()
                    continue
                stack.pop()
                k -= 1
            if(len(stack) ==  0 or num[i] != '0' or k == 0):
                stack.append(num[i])
        while len(stack) > 0 and k > 0:
            stack.pop()
            k -= 1
        ans = ''.join(stack)
        if(len(ans) == 0 or int(ans) == 0):
            return '0'
        
     
        return ans.lstrip('0')