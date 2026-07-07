class Solution:
    def numDecodings(self, s: str) -> int:
        codes = set(map(str, range(1, 27)))
        mem = {len(s): 1}

        def dfs(i: int) -> int:
            if i in mem:
                return mem[i]

            res = 0
            res += dfs(i+1) if i < len(s) and s[i] in codes else 0
            res += dfs(i+2) if i+2 <= len(s) and s[i:i+2] in codes else 0
            mem[i] = res
            return res

        return dfs(0)
 
        