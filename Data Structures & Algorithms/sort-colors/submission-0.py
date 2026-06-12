class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countSort(nums, [0, 1, 2])
        

def countSort(nums, keys):
    d = {
        key: 0 for key in keys
    }

    for num in nums:
        d[num] += 1

    i = 0
    for key in keys:
        while d[key] > 0:
            d[key] -= 1
            nums[i] = key
            i += 1