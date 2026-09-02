class Solution:
    def jump(self, nums: List[int]) -> int:
        """Button-up DP
        Time: O(n**2)
        Space: O(n)
        """
        N =  len(nums)
        cache = [float("inf")] * N
        cache[-1] = 0
        for i in reversed(range(N - 1)):
            j, jump = i + 1, min(nums[i], N)
            cache[i] = 1 + min(cache[j : j + jump], default=float("inf"))
            # print(f"{i=}, {cache=}")

        return cache[0]
