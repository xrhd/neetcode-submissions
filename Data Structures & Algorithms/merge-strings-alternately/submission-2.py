class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pre = "".join((a + b for a, b in zip(word1, word2)))
        if len(word1) == len(word2):
            return pre
        if len(word1) > len(word2):
            return pre + word1[len(word2) :]
        elif len(word1) < len(word2):
            return pre + word2[len(word1) :]
