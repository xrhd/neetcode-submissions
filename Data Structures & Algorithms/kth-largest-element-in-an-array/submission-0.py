class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Sort """
        nums.sort(reverse=True)
        return nums[k-1]
        