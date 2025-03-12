class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3 
        for num in nums:
            count[num] += 1 
        
        index = 0 
        for i in range(0, len(count)):
            while count[i] != 0:
                nums[index] = i
                count[i] -= 1 
                index += 1 
        
        