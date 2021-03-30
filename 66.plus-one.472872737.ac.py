class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = digits[:]
        for i in xrange(len(res) - 1, -1, -1):
            if res[i] == 9:
                res[i] = 0
            else:
                res[i] += 1
                return res
        res.insert(0, 1)
        return res
