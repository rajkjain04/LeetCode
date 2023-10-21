class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = [] 
        nums = sorted(nums)
        unique = set() 
        print(nums)
        
        for i in range(0, len(nums) - 2):
            
            first_value = nums[i]
            leftPointer = i + 1 
            rightPointer = len(nums) - 1
            
            while leftPointer < rightPointer: 
                second_value = nums[leftPointer]
                third_value = nums[rightPointer]
                
                if first_value + second_value + third_value == 0:
                    if (first_value, second_value, third_value) not in unique:
                        output.append([first_value, second_value, third_value])
                        unique.add((first_value, second_value, third_value))
                    
                    leftPointer += 1 
                    rightPointer -= 1
                
                elif first_value + second_value + third_value > 0:
                    rightPointer -= 1 
                
                else:
                    leftPointer += 1 
            
        return output 
                    
                
                
            
            
            

        
        
        