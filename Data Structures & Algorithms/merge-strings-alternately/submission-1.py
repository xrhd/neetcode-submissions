class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pre = "".join((a + b for a, b in zip(word1, word2)))
        pos = ""
        if len(word1) > len(word2):
            pos = word1[len(word2) :]
        elif len(word1) < len(word2):
            pos = word2[len(word1) :]
        return pre + pos
