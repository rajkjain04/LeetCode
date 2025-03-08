class TimeMap:

    def __init__(self):
        self.hashMap = {} 
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = [(value, timestamp)]
        
        else:
            self.hashMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        output = ""
        if key not in self.hashMap:
            return output 
        
        items = self.hashMap[key] 
        leftPointer = 0
        rightPointer = len(items) - 1 

        while leftPointer <= rightPointer:
            middlePointer = (leftPointer + rightPointer) // 2 

            value, time = items[middlePointer] 

            if time == timestamp:
                return value
            
            if time > timestamp: 
                rightPointer = middlePointer - 1 
            
            else:
                output = value 
                leftPointer = middlePointer + 1 

        return output  

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)