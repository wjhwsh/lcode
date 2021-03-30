class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        N = len(seats)
        findNext = (i for i in range(N) if seats[i])
        prev, future = None, next(findNext)
        ans = 0
        for i in range(N):
            if seats[i]:
                prev = i
            else:
                while future != None and future < i:
                    future = next(findNext, None)
                left = N if prev is None else i - prev
                right = N if future is None else future - i
                ans = max(ans, min(left, right))
        return ans
