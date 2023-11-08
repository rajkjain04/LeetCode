class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0 
        
        seen = set() 
        maxLen = 0 
        L = 0 
        R = 0 
        
        while R <= len(s) - 1:
            if s[R] not in seen:
                seen.add(s[R])
                maxLen = max(maxLen, len(seen))
                R += 1 
            
            else: 
                while s[R] in seen:
                    seen.remove(s[L]) 
                    L += 1     
            
        return maxLen 
   
                 