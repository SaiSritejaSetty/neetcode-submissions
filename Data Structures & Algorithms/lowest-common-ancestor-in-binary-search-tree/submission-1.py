# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(r,x,y):
            if x.val<r.val and y.val<r.val:
                if r.left:
                    left = r.left
                    return helper(left,x,y)
            elif x.val>r.val and y.val>r.val:
                if r.right:
                    right = r.right
                    return helper(right,x,y)
            elif (x.val>r.val and y.val<r.val) or x.val<r.val and y.val>r.val:
                return r
            elif x.val == r.val or y.val == r.val:
                return r 
            
        return helper(root,p,q)

                    

        