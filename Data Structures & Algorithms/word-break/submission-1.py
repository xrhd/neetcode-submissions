class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """DP with mem"""

        mem = {len(s): True}

        def dfs(i):
            nonlocal mem
            if i in mem:
                return mem[i]

            for w in wordDict:
                j = i + len(w)  # next index
                if j <= len(s) and s[i:j] == w and dfs(j):
                    mem[i] = True
                    return True

            mem[i] = False
            return False

        return dfs(0)
