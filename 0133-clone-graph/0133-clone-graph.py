"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = {} 
        stack = [node]
        
        if not node:
            return None
        
        clone_node = Node(node.val)
        visited[node] = clone_node       
        
        
        while stack:
            current_node = stack.pop() 
            
            for neighbour in current_node.neighbors:
                if neighbour not in visited:
                    clone_neighbour = Node(neighbour.val)
                    visited[neighbour] = clone_neighbour
                    
                    visited[current_node].neighbors.append(clone_neighbour)
                    stack.append(neighbour)
                    
                else:
                    visited[current_node].neighbors.append(visited[neighbour])
                    
                
        return clone_node
                    
                    
                
            
                
                    
                    
                    
                
                
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        