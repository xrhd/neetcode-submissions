class Solution:
    def jump(self, nums: List[int]) -> int:
        """Greedy BFS
        Time: O(n)
        Space: O(1)
        """
        R = len(nums) - 1  # most right index
        l = r = levels = 0  # init variables

        while r < R:
            l, r = r + 1, max((i + nums[i] for i in range(l, r + 1)))
            levels += 1
        return levels
