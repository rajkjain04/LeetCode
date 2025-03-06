class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        output = [0] * len(nums) 

        # 0 -> 3
        # 1 -> 4 
        # 2 -> 5 
        # 3 -> 6
        # 4 -> 0 

        for i in range(0, len(nums)):
            item = nums[i]
            index = (i + k) % len(nums)
            output[index] = item 
        
        for i in range(0, len(output)):
            nums[i] = output[i]

        