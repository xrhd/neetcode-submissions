class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {
            crs: [] for crs in range(numCourses)
        }
        for crs, pre in prerequisites:
            adj[crs].append(pre)


        visited = set()
        def dfs(crs: int) -> bool:
            nonlocal visited
            if crs in visited:
                return False # loop detected

            if not adj[crs]:
                return True # no pre req.

            visited.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            adj[crs] = [] # empty all pre reqs
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True 
        