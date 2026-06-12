class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return foo(0, nums, [])


def foo(i: int, nums: List[int], curr: List[int]) -> List[List[int]]:
    if i >= len(nums):
        return [curr]

    result = []
    result.extend(foo(i+1, nums, curr))
    result.extend(foo(i+1, nums, curr + [nums[i]]))
    return result