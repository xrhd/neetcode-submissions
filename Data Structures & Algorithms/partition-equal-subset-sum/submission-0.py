class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 !=0:
            return False

        target = total // 2
        parts = { 0 }
        for num in nums:
            parts |= {part + num for part in parts}
            if target in parts:
                return True

        return False