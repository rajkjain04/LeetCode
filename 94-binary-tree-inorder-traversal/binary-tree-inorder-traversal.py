# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        output = [] 
        if root is None:
            return output 

        curr = root
        stack = []

        while stack or curr:
            while curr:
                stack.append(curr) 
                curr = curr.left
            
            curr = stack.pop() 
            output.append(curr.val)
            curr = curr.right 
        
        return output
