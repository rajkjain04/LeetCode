class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {} 

        for i in range(0, len(nums)):
            value = nums[i] 

            if target - value in hashMap:
                return [i, hashMap[target -  value]]
            
            else: 
                hashMap[value] = i 

        