class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """1d DP solution
        time: O(n**2)
        space: O(n)
        """
        N = len(prices)
        if N <= 1:
            return 0

        profit = [0] * (N + 2)  # pontencial de ganhar a partido do indice i

        for i in range(N - 2, -1, -1):
            profit_ith = profit[i + 1]
            for j in range(i + 1, N):
                profit_ith = max(profit_ith, prices[j] - prices[i] + profit[j + 2])

            profit[i] = profit_ith
            # print(f"{profit=}")

        return profit[0]
