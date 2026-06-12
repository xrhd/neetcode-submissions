def symbol2value(c: str):
    match c:
        case "I":
            return 1
        case "V":
            return 5
        case "X":
            return 10
        case "L":
            return 50
        case "C":
            return 100
        case "D":
            return 500
        case "M":
            return 1000

class Solution:
    def romanToInt(self, s: str) -> int:
        res, m = 0, 0
        for c in reversed(s):
            v = symbol2value(c)
            if v >= m:
                res += v
            else:
                res -= v
            m = max(m, v)

        return res
        