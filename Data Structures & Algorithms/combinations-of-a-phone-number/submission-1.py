class Solution:
    def __init__(self):
        chars = [chr(97 + i) for i in range(26)]
        self.digits_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v",],
            "9": [ "w", "x", "y", "z"],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []

        def dfs(comb):
            nonlocal res
            i = len(comb)
            if i >= len(digits):
                res.append(comb)
                return

            for c in self.digits_map.get(digits[i]):
                dfs(comb + c)

        dfs("")
        return res
