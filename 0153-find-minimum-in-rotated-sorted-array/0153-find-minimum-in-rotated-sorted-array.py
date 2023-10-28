class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        leftPointer = 0 
        rightPointer = len(nums) - 1 
        minimum = float('inf')
        
        
        while leftPointer <= rightPointer: 
            middlePointer = (leftPointer + rightPointer) // 2 
            
            if nums[middlePointer] >= nums[leftPointer]:
                minimum = min(nums[leftPointer], minimum)
                leftPointer = middlePointer + 1 
                
            else: 
                minimum = min(nums[middlePointer], minimum)
                rightPointer = middlePointer - 1 
                
                
        return minimum 
                
                
        
        
        