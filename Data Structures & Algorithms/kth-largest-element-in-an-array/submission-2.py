import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Heap"""
        return heapq.nlargest(k, nums)[-1]
        