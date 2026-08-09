def minmax(nums):
    return min(nums), max(nums)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, cmin, cmax = float('-inf'), 1, 1
        for n in nums:
            if n == 0:
                cmin, cmax = 1, 1
            cmin, cmax = minmax((n * cmin, n * cmax, n))
            res = max(res, cmax)

        return res
