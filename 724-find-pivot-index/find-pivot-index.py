class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefixSums = []
        total = 0  
        for i in range(0, len(nums)):
            total += nums[i]
            prefixSums.append(total)
        
        for i in range(0, len(prefixSums)):
            if i == 0:
                if prefixSums[-1] - prefixSums[0] == 0:
                    return 0   
                continue 
            
            rightSum = prefixSums[-1] - nums[i] - prefixSums[i - 1]
            leftSum = prefixSums[i - 1]

            if rightSum == leftSum:
                return i 
            
        return -1 
            
