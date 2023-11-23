class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0 
        right = len(nums) - 1 
        
        while left <= right: 
            
            middle = (left + right) // 2 
            
            if (nums[middle] == target):
                return middle
            
            elif (nums[left] == target):
                return left 
            
            elif (nums[right] == target):
                return right
            
            if (nums[middle] >= nums[left]): 
                # Left Sorted Portion 
                if (nums[left] < target < nums[middle]):
                    right = middle - 1 
                
                else: 
                    left = middle + 1 
                
            else: 
                # Right Sorted Portion 
                if (nums[middle] < target < nums[right]):
                    left = middle + 1 
                    
                else: 
                    right = middle - 1 
                
            
        return -1 
            
        