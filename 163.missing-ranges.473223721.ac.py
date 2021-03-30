class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        prev = lower - 1
        for i in xrange(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 < curr:
                res.append((prev + 1, curr - 1))
            prev = curr
        return map(lambda x: str(x[0]) + "->" + str(x[1]) if x[0] < x[1] else str(x[0]), res)
