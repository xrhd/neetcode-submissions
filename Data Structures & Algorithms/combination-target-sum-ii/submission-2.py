class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        candidates = [num for num in candidates if num <= target]
        N = len(candidates)

        res = []

        def dfs(i:int, curr:list, total:int) -> None:
            nonlocal res
            if total == target:
                res.append(curr.copy())
                return 

            if total > target or i >= N:
                return

            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop()

            while i+1 < N and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
