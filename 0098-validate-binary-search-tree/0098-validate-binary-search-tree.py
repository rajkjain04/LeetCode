# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, lowerBound, upperBound):
            
            if not root:
                return True 
            
            if not (lowerBound < root.val < upperBound):
                return False 
            
            leftLowerBound = lowerBound 
            leftUpperBound = root.val 
            
            rightLowerBound = root.val 
            rightUpperBound = upperBound 
            
            x = dfs(root.left, leftLowerBound, leftUpperBound)
            y = dfs(root.right, rightLowerBound, rightUpperBound)
            
            return x and y 
            
        
        return dfs(root, float('-inf'), float('inf'))
        
        