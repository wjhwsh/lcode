from fractions import Fraction
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        hq = []

        k, N =0, len(quality)
        ans = float("inf")
        sumq = 0
        ratios = sorted([(Fraction(w, q), q, w) for q, w in zip(quality, wage)])
        
        for ratio, q, w  in ratios:
            sumq += q
            k += 1
            heapq.heappush(hq, -q)
            if k > K:
                sumq += heapq.heappop(hq)
                k -= 1
            if k == K:
                ans = min(ans, sumq * ratio)
        return ans
