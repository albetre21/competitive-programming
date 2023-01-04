class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        string = ""
        
        
        for i in range(len(s)):
            
            if s[i] =="[":
                stack.append(string)
                if i -1 >= 0:
                    temp = ""
                    j = i -1
                    while j >= 0  and s[j].isnumeric():
                        temp += s[j]
                        j-=1
                            
                    stack.append(temp[::-1])
                    string = ""
            elif s[i] == "]":
                temp = int(stack.pop())
                string = stack.pop() + string * temp
            elif s[i].isnumeric() == False:
                string += s[i]
            
        return string