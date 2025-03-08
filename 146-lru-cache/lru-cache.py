class Node: 
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.prev = None 
        self.next = None  

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} # map key to nodes 

        # Left = LRU, right = Most Recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    # Remove node from list
    def remove(self, node):
        prev = node.prev 
        prev.next = node.next 
        node.next.prev = prev
    
    # Insert node at right 
    def insert(self, node): 
        prevRight = self.right.prev
        prevRight.next = node 
        node.prev = prevRight
        node.next = self.right 
        self.right.prev = node 

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
            # remove from the list and delete the LRU from the cache 
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)