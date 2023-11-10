class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0,0]
        
        dp[0] = 1 
        dp[1] = 1 
        
        i = 2 
        
        while i <= n:
            tmp = dp[0] 
            dp[0] = dp[1] 
            dp[1] += tmp 
            i += 1 
            
        return dp[1]
            
            
            
            