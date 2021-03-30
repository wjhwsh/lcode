# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

class Solution(object):
    def __init__(self):
        self.buffer = [""] * 4
        self.buffer_index = 0
        self.buffer_len = 0
        
    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        copied_count = 0
        while copied_count < n:
            if self.buffer_index == 0:
                self.buffer_len = read4(self.buffer)
                if self.buffer_len == 0:
                    break
            while self.buffer_index < self.buffer_len and copied_count < n:
                buf[copied_count] = self.buffer[self.buffer_index]
                copied_count += 1
                self.buffer_index += 1
            if self.buffer_index >= self.buffer_len:
                self.buffer_index = 0
        return copied_count
