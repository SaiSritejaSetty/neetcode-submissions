# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque([root])
        res = []
        if not root:
            return []
        while stack:
            size = len(stack)
            lev = []
            for _ in range(size):
                r = stack.popleft()
                value = r.val
                lev.append(value)
                if r.right:
                    stack.append(r.right)
                if r.left:
                    stack.append(r.left)
            res.append(lev[0])
        return res
            


