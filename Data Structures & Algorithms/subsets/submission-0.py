class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        foo(0, nums, [], res)
        return res


def foo(i, nums, curr, res):
    if i >= len(nums):
        res.append(curr.copy())
        return

    foo(i+1, nums, curr, res)
    foo(i+1, nums, curr + [nums[i]], res)
