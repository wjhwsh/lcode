class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        if not s:
            return 0
        if len(s) == 1:
            return 1
        ans, i = 1, 0
        for k, v in enumerate(s):
            if v in seen:
                i = max(i, seen[v])
            seen[v] = k + 1
            ans = max(ans, k - i + 1)
        return ans
