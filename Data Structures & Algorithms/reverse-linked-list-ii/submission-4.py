# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        count = 1
        need = right - left + 1
        prev = dummy 
        while count!=left:
            prev = curr
            curr = curr.next
            count+=1
        if count == left:
            tail = curr
        prev1 = None
        while need > 0:
            nex = curr.next
            curr.next = prev1
            prev1 = curr
            curr = nex
            need-=1
        if need == 0:
            prev.next = prev1
            tail.next = curr
        return dummy.next
        
        