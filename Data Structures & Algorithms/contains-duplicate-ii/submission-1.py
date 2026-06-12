class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        bag, l = set(), 0

        for r, num in enumerate(nums):
            if num in bag:
                return True

            bag.add(num)

            if r - l + 1 > k:
                bag.remove(nums[l])
                l += 1

        return False


        