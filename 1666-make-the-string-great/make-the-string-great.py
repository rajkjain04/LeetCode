class Solution:
    def makeGood(self, s: str) -> str:

        stack = [s[0]] 

        for i in range(1, len(s)):
            character = s[i]
            
            if not character.islower():
                if stack and character.lower() == stack[-1]:
                    stack.pop() 
                    continue
            
            if stack and not stack[-1].islower() and stack[-1].lower() == character:
                stack.pop()
                continue 

            stack.append(character)

        result = ""
        for item in stack:
            result += item 
        
        return result 

        