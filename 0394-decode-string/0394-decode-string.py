class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = [] 
        digits = set(["0","1","2","3","4","5","6","7","8","9"]) 
        i = 0 
        output = ""
        
        while i < len(s): 
            value = s[i]
            
            if value != "]":
                stack.append(value)
                
            else: 
                substr = "" 
                while stack[-1] != "[":
                    item = stack.pop()
                    substr = item + substr  
                
                stack.pop() 
                number = ""
                
                while stack and stack[-1] in digits:
                    item = stack.pop() 
                    number = item + number 
                
                number = int(number)
                for k in range(1, number + 1):
                    stack.append(substr)         
            
            i += 1 
            
        output = ''.join(stack) 
            
        return output 
        
        
                
                
                
                
                
                
            
                