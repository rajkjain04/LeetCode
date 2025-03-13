class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1 
        sign = 0 
        
        for num in nums:
            if num == 0:
                return 0 
            
            if num > 0:
                if sign == 0 or sign == 1:
                    sign = 1

                else:
                    sign = -1     
            
            else:
                if sign == 0 or sign == 1:
                    sign = -1 
                
                else:
                    sign = 1
        
        return sign 
        