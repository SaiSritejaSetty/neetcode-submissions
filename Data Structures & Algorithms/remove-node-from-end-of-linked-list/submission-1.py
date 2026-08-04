# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            Nex = curr.next
            curr.next = prev
            prev = curr
            curr = Nex
        dummy = ListNode()
        count = 0
        dummy.next = prev
        cur = dummy
        while count<n-1:
            cur = cur.next
            count+=1
        cur.next = cur.next.next
        current=dummy.next
        prev1=None
        while current:
            Nexx = current.next
            current.next = prev1
            prev1 = current
            current = Nexx
        return prev1

        
        
             
        