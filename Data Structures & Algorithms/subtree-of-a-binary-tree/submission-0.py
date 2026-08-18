# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == subRoot:
            return True
        elif not root:
            return False

        

        def helper(x,y):
            if not x and not y:
                return True
            elif not x or not y:
                return False
            elif x.val != y.val:
                return False
            left = helper(x.left , y.left)
            right =helper(x.right, y.right)
            if right and left:
                return True
            else:
                return False
            
        if helper(root,subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))
        


            