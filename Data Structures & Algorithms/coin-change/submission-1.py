class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ Lets try a bottom up approach 
        """
        # maps amount -> min # of coins required
        mem = [
            float('inf') for _ in range(amount+1) # 0.., amount
        ]
        mem[0] = 0

        for am in range(1, amount+1): # 1.., amount
            candidates = (
                1 + mem[am - c]
                for c in coins
                if am - c >= 0
            )
            mem[am] = min(candidates, default=mem[am])

        return mem[amount] if mem[amount] != float('inf') else -1