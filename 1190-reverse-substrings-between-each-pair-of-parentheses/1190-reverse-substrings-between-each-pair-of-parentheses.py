class Solution:
    def reverseParentheses(self, s: str) -> str:
        n=len(s)
        stack=[]
        for i in range(n):
            if s[i]!=')':
                stack.append(s[i])
            else:
                ans=""
                while stack and stack[-1]!="(":
                    val=stack.pop()
                    ans+=str(val)
                stack.pop()
                for j in ans:
                    stack.append(j)
        return "".join(stack)