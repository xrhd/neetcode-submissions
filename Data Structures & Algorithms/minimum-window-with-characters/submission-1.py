def counter(s):
    res = {}
    for c in s:
        if c not in res:
            res[c] = 0
        res[c] += 1
    return res

def is_present(subc, tc):
    for k, v in tc.items():
        if subc.get(k, 0) < v:
            return False
    return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """O(s**2) time, O(s+t) space"""
        tc = counter(t)
        res = None
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub = s[i: j]
                subc = counter(sub)
                if is_present(subc, tc) and (not res or len(sub) < len(res)):
                    res = sub
        # empty
        return res if res else ""
        