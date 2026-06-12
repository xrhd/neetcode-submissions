from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        return next((
            k for k, v in counter.items()
            if v >= len(nums) // 2 + 1
        ))