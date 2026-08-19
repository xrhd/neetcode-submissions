class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """DFS topological sort"""
        adj = {u: set() for u in range(numCourses)}
        for u, v in prerequisites:
            adj[v].add(u)

        def dfs(u, adj, visited, path, top):
            if u in path:
                return True  # has cycle

            if u in visited:
                return False

            visited.add(u)
            path.add(u)
            for v in adj[u]:
                if dfs(v, adj, visited, path, top):
                    return True  # has cycle

            path.remove(u)
            top.append(u)

        visited, path, top = set(), set(), []
        has_cicle = False
        for u in range(numCourses):
            if dfs(u, adj, visited, path, top):
                return []

        return top[::-1]
