class MyStack:

    def __init__(self):
        self.queue = [] 

    def push(self, x: int) -> None:
        self.queue.append(x)
        
    def pop(self) -> int:
        i = 0 
        while i < len(self.queue) - 1: 
            x = self.queue.pop(0) 
            self.queue.append(x)
            i += 1
            
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[-1]
        

    def empty(self) -> bool:
        return self.queue == [] 
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()