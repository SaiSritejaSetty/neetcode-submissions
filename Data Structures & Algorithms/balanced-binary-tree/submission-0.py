# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            if l == -1 or r==-1:
                return -1 
            if abs(r-l) <= 1:
                height = 1 + max(r,l)
                return height
            return -1
        if helper(root)!= -1:
            return True
        return False
            


        



        
        