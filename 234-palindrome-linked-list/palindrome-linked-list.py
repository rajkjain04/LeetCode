# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Get to the middle of the Linked List 
        slow = head 
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the linked list from the middle 
        prev = None 
        curr = slow 
        while curr: 
            tmp = curr.next 
            curr.next = prev 
            prev = curr
            curr = tmp 

        # Check if the linked list is a palindrome
        while prev != None:
            val1 = head.val 
            val2 = prev.val 

            if val1 != val2:
                return False 
            
            head = head.next 
            prev = prev.next

        return True 
        
        