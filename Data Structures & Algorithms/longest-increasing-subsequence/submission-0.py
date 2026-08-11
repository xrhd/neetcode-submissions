class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """ DP """
        N = len(nums)
        mem = [1 for _ in range(N)]
        for i in reversed(range(N)):
            candidates = (
                1 + mem[j]
                for j in range(i+1, N)
                if nums[i] < nums[j]
            )
            mem[i] = max(candidates, default=1)
        return max(mem)

        