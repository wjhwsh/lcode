class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_s, stack_t = [], []
        for s in S:
            if s == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(s)
        for t in T:
            if t == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(t)
        return stack_t == stack_s
    

            
