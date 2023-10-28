class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0 
        
        leftPointer = 0 
        rightPointer = 1 
        
        while rightPointer < len(prices):
            if prices[leftPointer] > prices[rightPointer]:
                leftPointer = rightPointer
                rightPointer += 1 
                
            else:
                profit = max(prices[rightPointer] - prices[leftPointer], profit)
                rightPointer += 1 
                
        return profit 
            
            
        
        
        
        