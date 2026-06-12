from collections import deque



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque(maxlen=k)
        def add(i):
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)

        # init the window
        for i in range(k):
            add(i)

        # process
        res = [nums[d[0]]]
        for l, r in zip(
            range(1, len(nums)-k+1),
            range(k, len(nums))
        ):
            if l > d[0]:
                d.popleft()
            add(r)
            res.append(nums[d[0]])

        return res