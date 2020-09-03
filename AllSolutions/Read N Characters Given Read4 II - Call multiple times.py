"""
Read N Characters Given Read4 II - Call multiple times
"""

"""
这道题和I的主要区别是difference between single time and multiple time, 举例来说, 一个buff 10个字符
长, 使用 read(3), read(3), read(4), 这里第一次调用read(3)的时候,会读进去4个字符,
第二次调用read(3)的时候,需要处理之前多读的一个字符.

In both cases, buf only host non-empty elements in the form of list (a little tricky here as the OJ return is str while 
in function buf is a list.)
"""

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

"""
The main challenge is to deal with two situations:
- since we are always reading 4 from the file, we need to save the residual of the buffer when we just need some of it to fulfill our requirement
- when we are reading, we first need to consume the residual buffer
"""

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.residual = [] # only host non-empty elements
        
    def read(self, buf: List[str], n: int) -> int:
        # retrieve residual first
        cnt = min(len(self.residual), n)
        buf[:cnt] = self.residual[:cnt]
        self.residual = self.residual[cnt:]
        
		# call read4 if there are more chars to retrieve
        chars_read = 4 # decide on when to stop calling read4
        while cnt < n and chars_read == 4:
            self.residual = ['']*4
            chars_read = read4(self.residual) # only return non-empty values
            while self.residual and cnt < n:
                buf[cnt] = self.residual.pop(0) # buf has enough space
                cnt += 1

        return cnt