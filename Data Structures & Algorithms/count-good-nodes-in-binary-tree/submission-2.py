# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(node,maximum):
            nonlocal count
            if not node:
                return 0
            if node.val >= maximum:
                count +=1
            maximum = max(maximum,node.val)
            helper(node.left,maximum)
            helper(node.right,maximum)

        
        helper(root, root.val)
        return count 
            
            

        
