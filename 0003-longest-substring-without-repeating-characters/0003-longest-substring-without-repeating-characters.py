class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0 
        
        charSet = set() 
        L = 0 
        R = 1 
        maxLen = 1 
        charSet.add(s[L])
        
        while R <= len(s) - 1:
            
            if s[R] not in charSet:
                charSet.add(s[R]) 
                R += 1 
                maxLen = max(len(charSet), maxLen)
                
            
            else:
                maxLen = max(len(charSet), maxLen)
                
                while s[R] in charSet: 
                    charSet.remove(s[L])
                    L += 1 
                
                    
        return maxLen
                
                
            
            
        
        