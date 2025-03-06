class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Need to determine the speed k 

        leftPointer = 1
        rightPointer = max(piles)
        minSpeed = float('inf')

        while leftPointer <= rightPointer: 
            middlePointer = (leftPointer + rightPointer) // 2 

            hours = 0 
            for pile in piles:
                hours += math.ceil(pile / middlePointer)

            if hours > h: 
                leftPointer = middlePointer + 1 
            
            else: 
                minSpeed = min(minSpeed, middlePointer)
                rightPointer = middlePointer - 1 
        
        return minSpeed 