class Solution:
    def jump(self, nums: List[int]) -> int:
        """Button-up DP"""
        cache = [0] * len(nums)
        for i in reversed(range(len(nums) - 1)):
            if nums[i] == 0:
                cache[i] = float("inf")
                continue
            jump = min(nums[i], len(nums) - 1 - i)
            cache[i] = 1 + min(cache[i + 1 : i + 1 + jump], default=float("inf"))
            # print(f"{i=}, {cache=}")

        return cache[0]
