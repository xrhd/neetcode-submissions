class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        mem = {}
        def dfs(i):
            nonlocal mem
            if i in mem:
                return mem[i]
            
            mem[i] = True
            for jump_len in reversed(range(1, nums[i]+1)):
                if i + jump_len < N:
                    dfs(i + jump_len)

            return mem[i]
            
        dfs(0)
        return mem.get(N-1, False)

        