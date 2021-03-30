class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'}':'{', ']':'[', ')':'('}
        stack = []
        for v in s:
            if not v in dic:
                stack.append(v)
            else:
                if not stack or stack[-1] != dic[v]:
                    return False
                stack.pop()
        return len(stack) == 0
            
