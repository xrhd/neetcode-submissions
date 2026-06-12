class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i, j = 0, 0
        for c in cost:
            i, j = j, min(i, j) + c

        return min(i, j)
        