# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node):
    if not node:
        return True, 0

    l, l_h = dfs(node.left)
    r, r_h = dfs(node.right)
    return (
        l and r and abs(l_h-r_h)<=1,
        1+max(l_h, r_h)
    )
    

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res, _ = dfs(root)
        return res
        