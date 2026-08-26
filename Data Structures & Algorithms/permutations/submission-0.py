class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            aux = []
            r = len(perms[0])
            for p in perms:
                for i in range(r+1):
                    aux.append(
                        p[:i] + [n] + p[i:]
                    )
            perms = aux
        return perms
