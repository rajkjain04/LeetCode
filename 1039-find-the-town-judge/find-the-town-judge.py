class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        incoming = {}
        outgoing = {} 

        for i in range(1, n + 1):
            incoming[i] = 0 
            outgoing[i] = 0 
        
        for item in trust:
            i, j = item 
            incoming[j] += 1
            outgoing[i] += 1 
        
        potentialJudges = [] 

        for key, value in outgoing.items():
            if value == 0:
                potentialJudges.append(key)  

        for potentialJudge in potentialJudges:
            if incoming[potentialJudge] == n - 1:
                return potentialJudge 

        return -1 
