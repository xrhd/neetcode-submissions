class Solution:
    def mySqrt(self, x: int) -> int:        
        res, l, r = 0, 0, x
        while l <= r:
            m = (r+l)//2
            if x < m*m:
                r = m-1
            elif m*m < x:
                l = m+1
                res = m
            else:
                return m
        return res