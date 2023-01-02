class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op={
            "+":lambda a,b:a+b,
            "*":lambda a,b:a*b,
            "-":lambda a,b:a-b,
            "/":lambda a,b:int(a/b)
        }
        stack=[]
        for i in tokens:
            if i in op:
                b=stack.pop()
                a=stack.pop()
                stack.append(op[i](a,b))
            else:
                stack.append(int(i))
        
        return stack.pop()