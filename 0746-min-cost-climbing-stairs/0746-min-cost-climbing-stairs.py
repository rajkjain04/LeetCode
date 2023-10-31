class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0) 
        
        i = len(cost) - 3 
        
        while i >= 0:
            left_cost = cost[i] + cost[i + 1]
            right_cost = cost[i] + cost[i + 2]
            
            cost[i] = min(left_cost, right_cost)
            
            i -= 1 
            
        return min(cost[0], cost[1])
            