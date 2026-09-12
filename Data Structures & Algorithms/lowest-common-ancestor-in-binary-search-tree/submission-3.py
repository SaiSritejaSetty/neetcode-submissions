# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(node,x,y):
            if node.val > x and node.val > y:
                if node.left:
                    left = node.left
                    return helper(left,x,y)
            elif node.val < x and node.val < y:
                if node.right :
                    right = node.right
                    return helper(right,x,y)
            elif (node.val>x and node.val<y) or (node.val<x and node.val>y):
                return node 

            elif node.val == x or node.val ==y:
                return node
        
        return helper(root,p.val,q.val)



                    

        