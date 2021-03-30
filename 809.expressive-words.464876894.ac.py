class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if not S or not words:
            return 0
        gs = [(k, len(list(grp))) for k, grp in itertools.groupby(S)]
        ans = 0
        for w in words:
            gw = [(k, len(list(grp))) for k, grp in itertools.groupby(w)]
            gw_cr = zip(*gw)
            gs_cr = zip(*gs)
            if gw_cr[0] != gs_cr[0]:
                continue
            gw_ct = gw_cr[1]
            gs_ct = gs_cr[1]
            ans += all(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(gs_ct, gw_ct))
        return ans
            
