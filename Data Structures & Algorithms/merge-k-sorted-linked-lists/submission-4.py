# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        if length == 0:
            return None
        elif length == 1:
            return lists[0]
        while len(lists)>1:
            merged = []
            for i in range(0,len(lists),2):
                x = lists[i]
                if i+1<len(lists):
                    y = lists[i+1]
                else:
                    y = None
                merged.append(self.mergetwolists(x,y))
            lists=merged
        return lists[0]
                
    def mergetwolists(self,l1,l2):
        dummy = node = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next 
            elif l1.val > l2.val:
                node.next = l2
                l2 = l2.next  
            node = node.next
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        return dummy.next 