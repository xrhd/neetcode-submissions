class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem: dict = {0: 0} | {
            coin: 1 for coin in coins 
        } # amount: min # of coins

        def foo(amount) -> int | None:
            if amount < 0:
                return None

            if amount not in mem:
                n_coins = (
                    1 + foo(amount - coin) 
                    for coin in coins
                    if foo(amount - coin)
                )
                mem[amount] = min(n_coins, default=None)

            return mem[amount]

        res = foo(amount)
        return res if res is not None else -1