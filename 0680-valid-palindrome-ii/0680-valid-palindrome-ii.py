class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isValid(s, i, j):
            l = i
            r = j 
            
            while l <= r:
                if s[l] != s[r]:
                    return False 
                
                l += 1 
                r -= 1 
            
            return True 
        
        if isValid(s, 0, len(s) - 1):
            return True 
        
        l = 0 
        r = len(s) - 1 
        
        while l <= r:
            if s[l] != s[r]:
                return isValid(s, l + 1, r) or isValid(s, l, r - 1)
            
            l += 1 
            r -= 1 
        
        return False 
            
        