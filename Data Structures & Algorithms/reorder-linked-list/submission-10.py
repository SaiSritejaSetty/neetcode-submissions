class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ac = head
        slow = head 
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        nex = slow.next
        slow.next = None
        prev = None 
        while nex:
            nexx = nex.next
            nex.next = prev
            prev = nex
            nex = nexx
        dummy = node = ListNode()
        list1 = ac
        list2 = prev
        while list2:
            tmp1 = list1.next
            tmp2 = list2.next
            list1.next = list2
            list2.next = tmp1
            list1 =tmp1
            list2 = tmp2

            
