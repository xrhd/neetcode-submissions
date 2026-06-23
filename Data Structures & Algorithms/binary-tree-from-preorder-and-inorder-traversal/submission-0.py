# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder) -> Optional[TreeNode]:
            if not preorder:
                return None
            
            pivot = preorder[0]  # don't pop — just index
            mid = inorder.index(pivot)
            
            # Partitioning
            inorder_left = inorder[:mid]
            inorder_right = inorder[mid+1:]
            
            preorder_left = preorder[1:1+len(inorder_left)]
            preorder_right = preorder[1+len(inorder_left):]

            # Node construction
            node = TreeNode(val=pivot)            
            node.left = dfs(preorder_left, inorder_left)
            node.right = dfs(preorder_right, inorder_right)
            return node

        return dfs(preorder, inorder)