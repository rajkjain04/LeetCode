class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set() 
        
        L = 0 
        window.add(nums[L])
        
        for r in range(1, len(nums)):
            
            if len(window) >= k + 1:
                window.remove(nums[L])
                L += 1 
                
                window.add(nums[L])
            
            if nums[r] in window and L != r:
                return True 
            
            window.add(nums[r])
            
        return False 
        