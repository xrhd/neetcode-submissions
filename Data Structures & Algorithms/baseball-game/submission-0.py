class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for op in operations:
            match op:
                case "C":
                    if s:
                        last = s.pop(-1)
                case "+":
                    s.append(s[-1] + s[-2])
                case "D":
                    s.append(2*s[-1] if s else 0)
                case _:
                    s.append(int(op))

        # print(s)
        return sum(s)

        