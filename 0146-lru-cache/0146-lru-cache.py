class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.prev = None 
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} # Map Key to Nodes 
        self.left, self.right = Node(0,0), Node(0,0)
        
        # Left = LRU, Right = Most Recent 
        self.left.next = self.right
        self.right.prev = self.left
        
    # Remove Node from List 
    def remove(self, node):
        prev = node.prev 
        nxt = node.next 
        prev.next, nxt.prev = nxt, prev 
    
    # Insert Node at Right 
    def insert(self, node):
        tmp = self.right.prev 
        self.right.prev = node 
        tmp.next = node 
        node.next = self.right 
        node.prev = tmp
    
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
            # Remove and delete the LRU
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
            
            
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)