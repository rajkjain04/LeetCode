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
        # Get the middle of the Linked List 
        slow = head 
        fast = head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

        # Reverse the second half of the Linked List 
        prev = None  
        curr = slow 

        while curr: 
            tmp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = tmp 

        # Merge the two linked lists 
        dummy = head
        first, second = head, prev 

        while second.next: 
            tmp1, tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1 
            first, second = tmp1, tmp2 
