class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.next = None 
        self.prev = None 

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} 
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right 
        self.right.prev = self.left
        
    def insert(self, node):
        tmp = self.right.prev 
        tmp.next = node 
        self.right.prev = node 
        node.prev = tmp 
        node.next = self.right 
        
    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next = nxt 
        nxt.prev = prev 
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1 
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # Remove from the list and delete the LRU 
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
            
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)