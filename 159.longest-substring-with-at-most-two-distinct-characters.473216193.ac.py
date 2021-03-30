class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 3:
            return len(s)
        l = r = ans = 0
        seen = {}
        while r < len(s):
            seen[s[r]] = r
            if len(seen) == 3:
                del_idx = min(seen.values())
                del seen[s[del_idx]]
                l = del_idx + 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans
                
            
