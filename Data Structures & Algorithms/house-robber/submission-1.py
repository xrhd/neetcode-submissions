class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cache = {}
        def foo(i):
            if i < 0:
                return 0

            if i in cache:
                return cache[i]

            cache[i] =  max(
                nums[i] + foo(i-2), 
                foo(i-1)
            )
            return cache[i]

        return foo(len(nums)-1)
            