class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '').upper()
        N = len(S)
        num_groups = N // K
        short_len = N % K
        first_part = S[:short_len]
        ans = []
        if first_part:
            ans.append(first_part)
        pos = short_len
        for i in range(num_groups):
            ans.append(S[pos:pos + K])
            pos += K
        return '-'.join(ans)
        
