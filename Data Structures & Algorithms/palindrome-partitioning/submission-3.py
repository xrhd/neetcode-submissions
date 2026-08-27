def is_palindrome(s: str) -> bool:
    return s == s[::-1]


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i: int, part: list) -> None:
            nonlocal res
            if i >= len(s):
                res.append(part)
                return

            for j in range(i, len(s)):
                subs = s[i : j + 1]
                if is_palindrome(subs):
                    dfs(j + 1, part + [subs])

        dfs(0, [])
        return res
