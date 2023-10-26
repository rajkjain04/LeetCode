# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head 
        prev = ListNode(0, next = curr)
        dummy = ListNode(0, next = curr)
        seen = set()
        
        while curr: 
            if curr.val not in seen:
                seen.add(curr.val)
                prev = curr 
                curr = curr.next
                
            else: 
                prev.next = curr.next 
                curr = curr.next 
                
        return dummy.next 
                
            
            
        
        
          
        
        
        