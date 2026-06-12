class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return foo(0, sorted(nums), [])

def foo(i, nums, curr):
    if i >= len(nums):
        return [curr]

    # loop to find the index of the next element
    num_i, j = nums[i], i+1
    while j < len(nums) and num_i == nums[j]:
        j += 1

    res = []
    res.extend(foo(j, nums, curr))
    res.extend(foo(i+1, nums, curr+[nums[i]]))
    return res