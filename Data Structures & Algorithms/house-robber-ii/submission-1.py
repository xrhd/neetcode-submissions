class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def foo(i, nums, cache):
            if i < 0:
                return 0

            if i in cache:
                return cache[i]

            cache[i] =  max(
                nums[i] + foo(i-2, nums, cache), 
                foo(i-1, nums, cache)
            )
            return cache[i]

        return max(
            foo(len(nums)-2, nums[1:], {}), 
            foo(len(nums)-2, nums[:-1], {}), 
        )
           