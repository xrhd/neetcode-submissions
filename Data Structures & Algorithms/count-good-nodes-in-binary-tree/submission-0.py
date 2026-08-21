# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, gval = float("-inf")):
            if node is None:
                return 0
            
            goods = int(node.val >= gval)
            gval = max(node.val, gval)
            goods += dfs(node.left, gval)
            goods += dfs(node.right, gval)
            return goods

        return dfs(root)