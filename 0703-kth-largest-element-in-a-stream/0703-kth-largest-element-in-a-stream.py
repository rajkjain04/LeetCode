class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = [] 
        self.k = k 
        # Python function which creates a heap N log N
        heapq.heapify(self.minHeap)
        i = 0 
        while i <= len(nums) - 1:
            heapq.heappush(self.minHeap, nums[i])
            
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)
                
            i += 1 

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)