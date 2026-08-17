# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]
        ans = 0
        heights = {}
        while stack:
            node, t = stack.pop()
            if not node:
                continue 
            if not t:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                left = heights.get(node.left,0)
                right = heights.get(node.right, 0)
                heights[node] = 1+max(left,right)
                ans = max(ans,left+right)
        return ans