class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_string_size = min((
            len(s) for s in strs
        ))
        
        i = 0
        for _ in range(shortest_string_size):
            ith_character = strs[0][i]
            if any((s[i] != ith_character for s in strs)):
                break
            i += 1

        return strs[0][:i]