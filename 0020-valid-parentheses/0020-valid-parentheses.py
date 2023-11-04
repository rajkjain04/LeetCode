class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] 
        left_brackets = set()
        left_brackets.add("(")
        left_brackets.add("{")
        left_brackets.add("[")
        
        for i in range(0, len(s)):
            if s[i] in left_brackets:
                stack.append(s[i])
                
            else:
                if stack == []:
                    return False 
                
                last_item = stack[-1]
                
                if (last_item == "(" and s[i] == ")") or (last_item == "[" and s[i] == "]") or (last_item == "{" and s[i] == "}"):
                    stack.pop() 
                    
                else:
                    return False 
                
        return stack == []
                
                
            
            
        