# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return (0,0)
            lrob,lskip = helper(node.left)
            rrob, rskip = helper(node.right)

            rob = node.val + lskip + rskip
            skip = max(lrob,lskip) + max(rrob,rskip)    

            return (rob,skip)
        return max(helper(root))
            
            
            