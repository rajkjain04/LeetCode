class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0; 
        
        int leftPointer = 0; 
        int rightPointer = 1; 
        
        while (rightPointer <= prices.length - 1) {
            int currentProfit = prices[rightPointer] - prices[leftPointer]; 
            profit = Integer.max(profit, currentProfit); 
            
            if (prices[leftPointer] > prices[rightPointer]) {
                leftPointer = rightPointer; 
            }
            
            rightPointer += 1; 
        }
        
        return profit; 
        
                
    }
}