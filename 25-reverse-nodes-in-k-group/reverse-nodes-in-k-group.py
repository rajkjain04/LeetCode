# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Set dummy pointers 
        dummy = ListNode(0, head) 
        groupPrev = dummy 

        while True:
            # Get the kth node
            kth = self.getKth(groupPrev, k)
            if not kth:
                break 
            groupNext = kth.next 

            # Reverse the group 
            prev, curr = groupNext, groupPrev.next 
            
            while curr != groupNext:
                tmp = curr.next 
                curr.next = prev 
                prev = curr 
                curr = tmp
                
            # Set the kth node to the beginning
            tmp = groupPrev.next
            groupPrev.next = kth 
            groupPrev = tmp 

        return dummy.next 

    def getKth(self, curr, k):
        while curr and k > 0: 
            curr = curr.next 
            k -= 1 
        return curr



        