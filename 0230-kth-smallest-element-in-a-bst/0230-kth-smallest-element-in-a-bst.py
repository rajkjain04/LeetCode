# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = [] 
        output = [] 
        curr = root 
        n = 0 
        
        while curr or stack != []:
            while curr:
                stack.append(curr)
                curr = curr.left 
                
            curr = stack.pop() 
            output.append(curr.val) 
            n += 1 
            if (n == k):
                return output[-1]
            curr = curr.right 
            
        return output[k - 1]
        
        
        
        
        