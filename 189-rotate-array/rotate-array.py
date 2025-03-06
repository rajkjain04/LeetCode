class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Reverse the entire array 
        k = k % len(nums)

        def reverse(nums, leftPointer, rightPointer): 
            while leftPointer <= rightPointer:
                tmp = nums[leftPointer]
                nums[leftPointer] = nums[rightPointer]
                nums[rightPointer] = tmp
                leftPointer += 1 
                rightPointer -= 1 

            return nums

        nums = reverse(nums, 0, len(nums) - 1)
        nums = reverse(nums, 0, k - 1)
        nums = reverse(nums, k, len(nums) - 1)


        
        