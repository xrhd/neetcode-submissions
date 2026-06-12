def counter(s):
    res = {}
    for c in s:
        if c not in res:
            res[c] = 0
        res[c] += 1
    return res

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = counter(t)
        T = len(t_counter.keys())

        s_counter = {c: 0 for c in t_counter}
        S = 0
        
        res, res_len = (-1, -1), float('inf')

        l = 0
        for r, c in enumerate(s):
            if c not in t_counter:
                # irrelevant character
                continue

            s_counter[c] += 1
            if s_counter[c] == t_counter[c]:
                S += 1

            while S == T:
                if r-l+1 < res_len:
                    res, res_len = (l, r), r-l+1
                
                cl = s[l]
                if cl  in t_counter:
                    s_counter[cl] -= 1
                    if s_counter[cl] < t_counter[cl]:
                        S -= 1
                l += 1
        
        if res_len == float("inf"):
            return ""

        l, r = res
        return s[l: r+1]

            