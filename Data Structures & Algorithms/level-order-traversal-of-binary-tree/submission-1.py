# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = deque([root])
        res = []
        while stack:
            size = len(stack)
            curr = []
            for _ in range(size):
                n = stack.popleft()
                if not n:
                    return []
                value = n.val
                curr.append(value)
                if n.left:
                    stack.append(n.left)
                if n.right:
                    stack.append(n.right)
            res.append(curr)
        return res 
                    
            
            