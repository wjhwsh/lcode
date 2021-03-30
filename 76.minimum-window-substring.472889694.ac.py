class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_counts = collections.defaultdict(int)
        t_counts = collections.Counter(t)
        l = r = 0
        ans = float("inf"), None, None
        required = len(t_counts)
        formed = 0
        while r < len(s):
            c = s[r]
            s_counts[c] += 1
            if c in t and s_counts[c] == t_counts[c]:
                formed += 1
            while l <= r and formed == required:
                c = s[l]
                if r - l + 1 < ans[0]:
                    ans = r - l + 1, l, r
                s_counts[c] -= 1
                if c in t and s_counts[c] < t_counts[c]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[1] is None else s[ans[1] : ans[2] + 1]
            
                
        
                
                
                
            
        
        
