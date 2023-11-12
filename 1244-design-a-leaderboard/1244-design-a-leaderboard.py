class Leaderboard:

    def __init__(self):
        self.hashMap = {}
        
    def addScore(self, playerId: int, score: int) -> None:
        
        # O(N)
        
        if playerId in self.hashMap:
            self.hashMap[playerId] += score 
        
        else:
            self.hashMap[playerId] = score 
        
    def top(self, K: int) -> int:
        
        minHeap = [] 
        heapq.heapify(minHeap)
        
        # Time Complexity - O(N log K)
        # Space Complexity - O(K)
        
        for value in self.hashMap.values():
            heapq.heappush(minHeap, value)
            
            if len(minHeap) > K:
                heapq.heappop(minHeap)
                
        
        res = 0 
        
        while minHeap:
            res += heapq.heappop(minHeap)
        
        return res 
        
    def reset(self, playerId: int) -> None:
        
        self.hashMap[playerId] = 0 
        
        
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)