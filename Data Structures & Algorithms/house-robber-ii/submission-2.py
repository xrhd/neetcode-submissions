class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(
            foo(nums[1:]), 
            foo(nums[:-1]), 
        )
           
def foo(nums):
    a, b = 0, 0
    for num in nums:
        a, b = b, max(num+a, b)

    return b