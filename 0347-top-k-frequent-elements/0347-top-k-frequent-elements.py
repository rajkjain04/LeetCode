class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = {} 
        bucket_sort = [] 
        output = [] 
        
        for item in nums:
            if item not in hash_map:
                hash_map[item] = 1 
            
            else:
                hash_map[item] += 1 
                
        for i in range(len(nums) + 1):
            bucket_sort.append([]) 
            
        for key, value in hash_map.items():
            index = value 
            bucket_sort[index].append(key)
        
        for i in range(len(bucket_sort) - 1, -1, -1):
            
            if k == 0:
                return output
            
            if bucket_sort[i] != []:
                while bucket_sort[i] != [] and k > 0:
                    val = bucket_sort[i].pop() 
                    output.append(val)
                    k -= 1 
                
        return output 
        
        