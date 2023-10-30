# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(0, next = head)
        
        fast = head 
        slow = head
        
        while fast and fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next 
            
        if fast.next:
            fast = fast.next
        
        prev = None 
        
        while slow:
            tmp = slow.next 
            slow.next = prev
            prev = slow 
            slow = tmp 
            
        while head:
            tmpHead = head.next 
            tmpPrev = prev.next
            head.next = prev 
            prev.next = tmpHead 
            head = tmpHead 
            prev = tmpPrev
            
            
            
        
        