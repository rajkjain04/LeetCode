class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = {} 
        output = [] 
        bucket_sort = [] 
        
        for i in range(0, len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1 
                
            else:
                hash_map[nums[i]] += 1 
                
        for i in range(0, len(nums) + 1):
            bucket_sort.append([])
            
        for key, value in hash_map.items():
            bucket_sort[value].append(key)
            
        index = len(bucket_sort) - 1
        temp_value = k 
        
        while k != 0:                 
            if bucket_sort[index] != []:
                output.extend(bucket_sort[index])
                if len(output) == temp_value: 
                    return output 
                k -= 1 
            index -= 1 
            
        return output 
        
        