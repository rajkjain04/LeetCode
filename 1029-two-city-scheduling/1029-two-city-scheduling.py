class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        output = [] 
        total_cost = 0 
        
        for i in range(0, len(costs)):
            city_a_cost = costs[i][0]
            city_b_cost = costs[i][1] 
            
            diff = city_b_cost - city_a_cost 
            output.append((diff, city_a_cost, city_b_cost))
            
        output = sorted(output)
        
        print(output)
        
        for i in range(0, len(output) // 2):
            total_cost += output[i][2]
        
        
        for j in range(len(output) // 2, len(output)):
            total_cost += output[j][1]
        
        return total_cost
        
        