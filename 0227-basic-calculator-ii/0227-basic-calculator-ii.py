class Solution:
    def calculate(self, s: str) -> int:
        current = counter = result = last = 0
        operator = '+'
        while(counter < len(s)):
            if(s[counter].isnumeric()):
            
                while(counter < len(s) and s[counter].isnumeric()):
                
                    current = current * 10 + int(s[counter])
                    counter += 1
                counter -= 1
            
                if operator == "+":
                    result += current
                    last = current
                elif operator == '-':
                    result -= current
                    last = -current
                elif operator == "*":
                    result -= last
                    
                    result += last * current
                    last = last * current
                else:
                    result -= last
                    result += int(last /current)
                    last = int(last/current)
                current = 0
            
            elif s[counter].isspace():
                counter += 1
                continue
            else:
                operator = s[counter]
                
            counter += 1
            
            
        return result