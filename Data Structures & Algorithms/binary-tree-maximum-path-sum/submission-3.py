# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node, global_path_sum=float('-inf')):
    if node is None:
        return 0, global_path_sum

    left, global_path_sum = dfs(node.left, global_path_sum) 
    right, global_path_sum = dfs(node.right, global_path_sum)
    
    # A path can only extend through one branch to its parent
    curr_node_branch_sum = node.val + max(left, right, 0)
    
    # A path can turn at this node, combining both branches
    curr_node_arch_sum = node.val + max(0, left) + max(0, right)
    
    global_path_sum = max(
        global_path_sum, 
        curr_node_arch_sum
    )
    return curr_node_branch_sum, global_path_sum
        

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        _, res = dfs(root)
        return res