class RandomizedSet:

    def __init__(self):
        self.lst = [] 
        self.hashMap = {} 
        
    def insert(self, val: int) -> bool:
        if val not in self.hashMap:
            self.lst.append(val)
            index = len(self.lst) - 1 
            self.hashMap[val] = index 
            return True 
            
        return False
        
    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            lastVal = self.lst.pop() 
            index = self.hashMap[val] 
            del self.hashMap[val] 
            
            if lastVal != val:
                self.lst[index] = lastVal
                self.hashMap[lastVal] = index 
                
            return True 
            
        return False 

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()