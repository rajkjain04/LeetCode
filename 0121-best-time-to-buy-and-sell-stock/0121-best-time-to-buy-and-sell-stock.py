class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0 
        L = 0 
        R = 1 
        
        while R <= len(prices) - 1: 
            currProfit = prices[R] - prices[L]
            profit = max(currProfit, profit) 
            
            if prices[L] > prices[R]:
                L = R 
                
            R += 1 
        
        return profit 
        