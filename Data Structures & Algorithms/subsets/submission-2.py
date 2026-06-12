class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, sub):
            if i >= len(nums):
                res.append(sub)
                return

            dfs(i+1, sub + [nums[i]])
            dfs(i+1, sub)

        dfs(0, [])
        return res