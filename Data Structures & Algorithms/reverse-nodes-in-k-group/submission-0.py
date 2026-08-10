# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        no_of_k = count // k
        
        dummy.next = head
        curr = head
        group_prev = dummy
        for x in range(no_of_k):
            group_start = group_prev.next
            curr = group_start
            prev = None
            for y in range(k):
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            group_prev.next = prev    
            group_start.next = curr         
            group_prev = group_start 
        return dummy.next
        
        
