# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        summ = float("-inf")
        def helper(node):
            nonlocal summ
            if not node:
                return 0

            left = max(helper(node.left),0)
            right = max(helper(node.right),0)
            res = node.val + left + right
            summ = max(res,summ)
            return node.val + max(left,right)
        helper(root)
        return summ


        
            

        