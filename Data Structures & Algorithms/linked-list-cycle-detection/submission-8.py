# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head 
        cur = head
        if not cur:
            return False
        while cur.next and cur.next.next:
            curr = curr.next
            cur = cur.next.next
            if curr == cur:
                return True 
        return False