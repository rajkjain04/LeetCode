class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] 
        output = [0] * len(temperatures)

        for i in range(0, len(temperatures)):
            if not stack or temperatures[i] < stack[-1][-1]:
                stack.append((i, temperatures[i]))
                continue 
            
            while stack and temperatures[i] > stack[-1][-1]:
                lastTuple = stack.pop()
                lastIndex = lastTuple[0]
                lastTemperature = lastTuple[1] 
                output[lastIndex] = i - lastIndex 
            
            stack.append((i, temperatures[i]))
            

        return output 
        