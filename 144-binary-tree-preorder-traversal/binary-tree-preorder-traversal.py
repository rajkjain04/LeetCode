# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        output = [] 
        if root is None: 
            return output 

        stack = [root] 

        while stack: 
            curr = stack.pop() 
            output.append(curr.val) 

            if curr.right:
                stack.append(curr.right)
            
            if curr.left: 
                stack.append(curr.left)

        return output
