class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """2d DP solution
        time: O(n)
        space: O(n)
        """
        N = len(prices)
        if N <= 1:
            return 0

        cache = {key: [0] * (N + 2) for key in ["buy", "sell"]}

        for i in range(N - 1, -1, -1):
            # if you buy at ith price
            profit = cache["sell"][i + 1] - prices[i]
            cache["buy"][i] = max(profit, cache["buy"][i + 1])
            # if you pass
            profit = cache["buy"][i + 2] + prices[i]
            cache["sell"][i] = max(profit, cache["sell"][i + 1])

        return cache["buy"][0]
