class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """O(1) Space"""
        m, n = len(matrix), len(matrix[0])
        set_c_to_zeros, set_r_to_zeros = False, False 

        if any(matrix[r][0]==0 for r in range(m)):
            set_c_to_zeros = True # need to set first col to zero 

        if any(matrix[0][c]==0 for c in range(n)):
            set_r_to_zeros = True # need to set up row to zero 
            
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        # select rows and cols
        cols = (c for c in range(1, n) if matrix[0][c] == 0)
        rows = (r for r in range(1, m) if matrix[r][0] == 0)

        # set to zero
        for c in cols:
            for r in range(1, m):
                matrix[r][c] = 0

        for r in rows:
            for c in range(1, n):
                matrix[r][c] = 0

        # check fist rows and cols
        if set_c_to_zeros:
            for r in range(m):
                matrix[r][0] = 0

        if set_r_to_zeros:
            for c in range(n):
                matrix[0][c] = 0
