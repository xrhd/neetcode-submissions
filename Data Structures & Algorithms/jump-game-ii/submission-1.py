class Solution:
    def jump(self, nums: List[int]) -> int:
        """Button-up DP"""
        cache = [float("inf")] * len(nums)
        cache[-1] = 0
        for i in reversed(range(len(nums) - 1)):
            j, jump = i + 1,  min(nums[i], len(nums))
            cache[i] = 1 + min(cache[j: j + jump], default=float("inf"))
            # print(f"{i=}, {cache=}")

        return cache[0]
