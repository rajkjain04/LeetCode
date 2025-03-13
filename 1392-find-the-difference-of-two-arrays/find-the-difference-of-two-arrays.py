class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        uniqueSet1 = set(nums1)
        uniqueSet2 = set(nums2)

        output = [[], []] 

        for num in uniqueSet1:
            if num not in uniqueSet2:
                output[0].append(num)
        
        for num in uniqueSet2:
            if num not in uniqueSet1:
                output[1].append(num)
            
        return output 
