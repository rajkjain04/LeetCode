class UndergroundSystem:

    def __init__(self):
        self.averageTimes = {} 
        self.checkInMap = {} 
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        srcName, timeIn = self.checkInMap[id]
        totalTime = t - timeIn
        
        if (srcName, stationName) not in self.averageTimes:
            self.averageTimes[(srcName, stationName)] = (totalTime, 1)
             
        else:
            currentTime, totalJourneys = self.averageTimes[(srcName, stationName)]
            totalPrevTime = currentTime * totalJourneys
            averageTime = (totalPrevTime + totalTime) / (totalJourneys + 1)
            
            self.averageTimes[(srcName, stationName)] = (averageTime, totalJourneys + 1) 
            
        self.checkInMap.pop(id)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return self.averageTimes[(startStation, endStation)][0]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)