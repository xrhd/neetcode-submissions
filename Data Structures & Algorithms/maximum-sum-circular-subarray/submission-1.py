class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax, gmin, total = float('-inf'), float('inf'), 0
        cmax, cmin = 0, 0
        for num in nums:
            cmax = max(cmax+num, num)
            gmax = max(gmax, cmax)

            cmin = min(cmin+num, num)
            gmin = min(gmin, cmin)
            total += num

        if gmax < 0:
            return gmax

        return max(gmax, total - gmin)
