from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        has_cycle = False 
        def dfs(n: int, prev:int = -1, vis:set = set()):
            nonlocal has_cycle
            res = {n}
            nxt = adj[n] - {prev}
            if not nxt:
                return res
            
            if nxt & vis:
                has_cycle = True
                return res 

            vis.add(prev)
            for node_nxt in nxt:
                res |= dfs(node_nxt, n, vis)
            vis.remove(prev)

            return res

        return len(dfs(0)) == n and not has_cycle