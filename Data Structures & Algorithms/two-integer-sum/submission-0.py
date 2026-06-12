class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux = {}
        for j, n in enumerate(nums):
            if n in aux:
                return [aux[n], j]
            aux[target - n] = j

        return [0, 0] 