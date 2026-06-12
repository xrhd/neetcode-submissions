class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, s, l):
            if s >= target or i >= len(nums):
                if s == target:
                    res.append(l)
                return
            
            num = nums[i]
            dfs(i, s + num, l + [num])
            dfs(i+1, s, l)

        dfs(0, 0, [])
        return res
        