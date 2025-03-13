class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        uniqueSet1 = set(nums1)
        uniqueSet2 = set(nums2)

        output = [[], []] 

        for num in nums1:
            if num not in uniqueSet2:
                output[0].append(num)
                uniqueSet2.add(num)
        
        for num in nums2:
            if num not in uniqueSet1:
                output[1].append(num)
                uniqueSet1.add(num)
            
        return output 
