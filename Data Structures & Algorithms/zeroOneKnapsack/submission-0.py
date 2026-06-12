class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}
        def foo(i, capacity):
            if i == len(profit):
                return 0

            if (i, capacity) in cache:
                return cache[(i,capacity)]

            cache[(i,capacity)] = foo(i+1, capacity)
            
            new_cap = capacity - weight[i]
            if new_cap >= 0:
                aux = profit[i] + foo(i+1, new_cap)
                cache[(i,capacity)] = max(cache[(i,capacity)], aux)

            return cache[(i,capacity)]

        return foo(0, capacity)

            