class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num2) - 1, -1, -1):
            for j in range(len(num1)-1, -1, -1):
                p = i + j + 1
                k = int(num2[i]) * int(num1[j]) + res[p]
                res[p] = (k % 10)
                res[p-1] += k // 10
        i = 0 if res[0] != 0 else 1
        return "".join(map(lambda x: str(x), res[i:]))

    
