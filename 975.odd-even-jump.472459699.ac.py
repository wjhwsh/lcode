class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        N = len(arr)

        def makeJumpNext(arr):
            ans = [None] * N
            stack = []
            for i in arr:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans
        
        sorted_arr = sorted(range(N), key = lambda i: arr[i])
        odd_next = makeJumpNext(sorted_arr)

        sorted_arr = sorted(range(N), key = lambda i: -arr[i])
        even_next = makeJumpNext(sorted_arr)
        odd, even = [False] * N, [False] * N
        odd[N-1] = even[N-1] = True

        for i in range(N-1, -1, -1):
            if odd_next[i] is not None:
                odd[i] = even[odd_next[i]]
            if even_next[i] is not None:
                even[i] = odd[even_next[i]]
        return sum(odd)
        
