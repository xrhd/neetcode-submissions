class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        for i in range(N//2):
            j = N-1-i
            s[i], s[j] = s[j], s[i]
        