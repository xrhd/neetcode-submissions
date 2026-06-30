class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        def opt(i, j):
            try:
                return words[i][j]
            except:
                return ""

        n = max(len(w) for w in words)
        n = max(n, len(words)) 
        for i in range(n):
            for j in range(n):
                if  opt(i, j) != opt(j, i):
                    return False

        return True