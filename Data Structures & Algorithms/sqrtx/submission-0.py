class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        l, r = 0, x//2
        while l < r:
            mid = (l+r)//2
            print(l, mid, r)
            mid_sqr = mid * mid
            if x < mid_sqr:
                r = mid-1
            elif mid_sqr < x:
                l = mid+1
                if x < l*l:
                    return mid
            else:
                return mid

        return l 