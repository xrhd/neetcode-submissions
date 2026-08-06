class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Naive vector approach with visited set
        """
        # direction vector 
        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        ]
        def rotate(direction):
            i = directions.index(direction)
            # print(f"{direction=}, {i=}, {j=}")
            return directions[(i+1) % 4]
        
        # bounderies
        n, m = len(matrix), len(matrix[0])
        def isinbound(point):
            x, y = point
            if 0 <= x < m and 0 <= y < n:
                return True
            return False

        # iterate
        p = (0, 0)
        direction = directions[0]
        vis = {p}
        res = [matrix[0][0]]
        N = n*m
        while len(res) < N:
            q = (p[0]+direction[0], p[1]+direction[1])
            if isinbound(q) and not q in vis:
                p = q
                vis.add(p)
                res.append(matrix[p[1]][p[0]])
            else:
                direction = rotate(direction)

        return res
        