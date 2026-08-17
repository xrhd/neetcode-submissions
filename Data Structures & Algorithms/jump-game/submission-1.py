class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """ Greedy solution """
        r = len(nums)-1
        l = r -1
        while l >= 0:
            jump_len = nums[l]
            # print(f"{l=}, {jump_len=}, {r=}")
            if l + jump_len >= r:
                r = l
            l -= 1
            
        return r == 0
        