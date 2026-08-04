class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # split — this makes first the bigger/equal half
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        # reverse second half
        prev1 = None
        curr = second
        while curr:
            Nex = curr.next
            curr.next = prev1
            prev1 = curr
            curr = Nex
        # merge — loop on second (the smaller half)
        first = head
        second = prev1
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            



        

        