# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast = head 
        slow = head 
        
        while True: 
            if ((fast and fast.next is None) or fast is None):
                return slow 
            
            fast = fast.next.next
            slow = slow.next
            
            
            
            
            
            
            
            
            
            
        
        
        