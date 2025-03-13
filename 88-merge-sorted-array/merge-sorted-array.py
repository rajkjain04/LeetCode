class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1 
        k = len(nums1) - 1 

        while j >= 0 and i >= 0:
            val1 = nums1[i]
            val2 = nums2[j] 

            if val2 > val1: 
                nums1[k] = val2
                j -= 1 
            
            else:
                nums1[k] = val1 
                i -= 1 

            k -= 1
        
        while j >= 0:
            nums1[k] = nums2[j] 
            k -= 1
            j -= 1 
        