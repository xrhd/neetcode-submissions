# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'N'

        res = []
        def pre(node):
            nonlocal res
            if node is None:
                res.append('N')
                return

            res.append(str(node.val))
            pre(node.left)
            pre(node.right)

        pre(root)
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:        
        vals = data.split(',')
        def dfs(i):
            if vals[i] == 'N':
                return None, i+1

            node = TreeNode(int(vals[i]))
            i += 1
            node.left, i = dfs(i)
            node.right, i = dfs(i)
            return node, i
        
        root, _ = dfs(0)
        return root

            
        
        
        