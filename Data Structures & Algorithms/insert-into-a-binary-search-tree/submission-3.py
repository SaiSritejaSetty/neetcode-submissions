# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node,v):
            if not node:
                return TreeNode(v)
            if node.val<v:
                node.right = helper(node.right,v)
            elif node.val>v:
                node.left = helper(node.left,v)
            return node
        return helper(root,val)

        
        
            