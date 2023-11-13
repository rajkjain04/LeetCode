class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = [] 
        self.graph = {} 
        
        for i in range(len(graph)):
            self.graph[i] = graph[i]
            
        def dfs(curr_path, curr_node): 
            if (curr_node) == len(self.graph) - 1:
                res.append(list(curr_path))
                
            for connection in self.graph[curr_node]:
                curr_path.append(connection)
                dfs(curr_path, connection) 
                curr_path.pop() 
                
        dfs([0], 0)
        
        return res 
            
            
            
            
            
        