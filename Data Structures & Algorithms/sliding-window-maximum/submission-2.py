from collections import deque



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque(maxlen=k)
        def add(i):
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)

        for i in range(k):
            add(i)

        res = [nums[d[0]]]

        l, r = 1, k
        while r < len(nums):            
            if l > d[0]:
                d.popleft()
            add(r)
            res.append(nums[d[0]])
            l += 1
            r += 1
            print(d)

        return res