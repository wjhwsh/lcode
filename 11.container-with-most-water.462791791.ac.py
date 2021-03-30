class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j, ans = 0, len(height) - 1, 0
        while i < j:
            ans = max(ans, min(height[i], height[j]) * ( j - i) )
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return ans
            
