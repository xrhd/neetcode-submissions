import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Sort """
        return heapq.nlargest(k, nums)[-1]
        