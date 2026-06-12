# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def foo(s, e):
            if e-s < 1:
                return

            pivot = pairs[e].key
            left = s

            # left partition
            for i in range(s, e):
                if pairs[i].key < pivot:
                    pairs[left], pairs[i] = pairs[i], pairs[left]
                    left += 1

            # swap pivot
            pairs[left], pairs[e] = pairs[e], pairs[left]

            # call recursion
            foo(s, left-1)
            foo(left+1, e)


        foo(0, len(pairs)-1)
        return pairs
        
        