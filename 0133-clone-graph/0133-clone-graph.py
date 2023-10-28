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
        
        if not node:
            return None 
        
        visited = {} 
        clone_node = Node(node.val, [])
        visited[node] = clone_node
        stack = [node]
        
        while stack:
            current_node = stack.pop() 
            
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    new_node = Node(neighbor.val, [])
                    visited[neighbor] = new_node 
                    visited[current_node].neighbors.append(new_node)
                    stack.append(neighbor)
                    
                else:
                    visited[current_node].neighbors.append(visited[neighbor])
                    
        return clone_node
                    
                    
                
            
                
                    
                    
                    
                
                
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        