# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string = []
        def helper(node):
            if not node:
                string.append('n')
                return
            curr = node
            value = curr.val
            string.append(str(value))
            helper(node.left)
            helper(node.right)
        helper(root)
        return ",".join(string)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(",")
        i = 0
        def helper():
            nonlocal i 
            if tokens[i] != 'n':
                new = TreeNode(int(tokens[i]))
                i+=1
            else:
                i+=1
                return None
            new.left = helper()
            new.right = helper()
            return new
        return helper()
        
            

                



