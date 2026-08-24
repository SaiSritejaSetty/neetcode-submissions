# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {}
        for pos in range(len(inorder)):
            idx[inorder[pos]] = pos

        def helper(preL, preR, inL, inR):
            if preL > preR:
                return None
            val = preorder[preL]
            root = TreeNode(val)
            j = idx[val]
            leftSize = j - inL
            root.left  = helper(preL + 1, preL + leftSize, inL, j - 1)
            root.right = helper(preL + leftSize + 1, preR, j + 1, inR)
            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)