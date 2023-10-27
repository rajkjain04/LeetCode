# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        right = head 
        dummy = ListNode(0, next = head)
        left = dummy 
        
        difference = n 
        
        while difference != 0:
            right = right.next 
            difference -= 1 
            
        while right != None:
            left = left.next 
            right = right.next 
            
        left.next = left.next.next 
        return dummy.next 
            
        
        
        