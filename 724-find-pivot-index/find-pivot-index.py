class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total = sum(nums)

        leftSum = 0 
        for i in range(0, len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i 
            
            leftSum += nums[i]

        return -1 