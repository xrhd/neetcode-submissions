class Solution:

    def encode(self, strs: List[str]) -> str:
        """ O(len(strs))"""
        sufix = [
            f'{len(s)}#' for s in strs
        ]
        return ''.join(map(lambda t: t[0]+t[1], zip(sufix, strs)))

    def decode(self, s: str) -> List[str]:
        """ O(len(s))"""
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            s_len = int(s[i:j])
            res.append(s[j+1:j+1+s_len])
            i = j+1+s_len
        return res