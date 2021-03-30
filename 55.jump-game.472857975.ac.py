class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        endIndex = N - 1
        for i in range(N-2, -1, -1):
            if nums[i] + i >= endIndex:
                endIndex = i
        return endIndex == 0
