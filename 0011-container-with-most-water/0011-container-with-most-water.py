class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxArea = 0 
        
        leftPointer = 0 
        rightPointer = len(height) - 1  
        
        while rightPointer > leftPointer:
            maxArea = max(maxArea, min(height[leftPointer], height[rightPointer])*(rightPointer - leftPointer))
            
            if height[rightPointer] > height[leftPointer]:
                leftPointer += 1 
                
            else:
                rightPointer -= 1 
                
        return maxArea 
                
            