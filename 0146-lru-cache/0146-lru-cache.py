class Node: 
    def __init__(self, key, val):
        self.key = key 
        self.val = val
        self.prev = None 
        self.next = None 

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} 
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right 
        self.right.prev = self.left 
    
    # Removes the provided node 
    def remove(self, node):
        left = node.prev 
        right = node.next 
        left.next = right 
        right.prev = left 
        
    # Inserts the node at the end of the list (before the right node) 
    def insert(self, node):
        prevNode = self.right.prev
        self.right.prev = node 
        node.next = self.right
        node.prev = prevNode
        prevNode.next = node 
    
    def get(self, key: int) -> int:    
        if key in self.cache: 
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val 
            
        return -1 
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
         
        node = Node(key, value)
        self.cache[key] = node 
        self.insert(node)
        
        if len(self.cache) > self.cap:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)