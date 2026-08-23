# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            values.append(node.val)
            helper(node.right)
        helper(root)
        while k > 1:
            values.pop(0)
            k-=1
        res = values[0]
        return res
        
