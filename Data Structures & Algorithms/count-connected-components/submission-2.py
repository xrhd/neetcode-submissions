from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set) 
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        def dfs(node, prev, visited):
            if not adj[node] - {prev}:
                return {node}

            components = {node}
            visited.add(node)
            for node_adj in adj[node] - {prev} - visited:
                components |= dfs(node_adj, node, visited)
            return components

        unique = set()
        visited = set()
        for node in range(n):
            if node not in visited:
                components = frozenset(dfs(node, -1, set()))
                unique.add(components)

        return len(unique)