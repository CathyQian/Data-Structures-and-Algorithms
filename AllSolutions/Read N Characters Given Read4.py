"""
Read N Characters Given Read4

https://leetcode.com/problems/read-n-characters-given-read4/
"""

"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
"""
Note: buf is predefined with enough space; need to define a buf4 in the read function
buf won't be returned but will be checked in OJ.

buf and buf4 are both lists of str and can be modified.
"""
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        res = 0
        buf4 = [' ']*4
        for i in range(n//4+1):
            cur = read4(buf4)
            if cur == 0:
                break
            buf[res:res+4]=buf4
            res += cur
        for j in range(n, res):
            buf[j] = ' '
        return min(res, n)
