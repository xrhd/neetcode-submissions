from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k, v = 0, 0
        for num in nums:
            if v == 0:
                k = num
            v += 1 if num == k else -1
        return k