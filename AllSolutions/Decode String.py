"""
Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that 
k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For
example, there won't be input like 3a or 2[4].
 
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

"""
"""
special attention: there may be nested []
so we can not scann the string from left to right and get the results directly
"""
# recursion, easier, less prone to make mistakes
class Solution:
    def decodeString(self, s: str) -> str:
        res, _ = self.decode(s, 0)
        return res
    
    def decode(self, s: str, i: int) -> str:
        res = ""
        while i < len(s) and s[i] != ']': # pay attention to while loop termination condition
            if 'a' <= s[i].lower() <= 'z': # str
                res += s[i]
                i += 1
            else:
                cnt = 0
                while '0' <= s[i] <= '9': # digit
                    cnt = cnt * 10 + int(s[i])
                    i += 1
                i += 1 # skip '['
                t, i = self.decode(s, i)
                i += 1 # skip ']'
                res += t*cnt
        return res, i

# iterative method using stack
class Solution:
    def decodeString(self, s: str) -> str:
        t = ""
        s_num, s_str = [], []
        cnt = 0
        for i in range(len(s)):
            if '0'<= s[i] <= '9':
                cnt = 10 * cnt + int(s[i])
            elif s[i] == '[':
                s_num.append(cnt)
                s_str.append(t)
                cnt = 0
                t = ''
            elif s[i] == ']':
                k = s_num.pop() 
                s_str[-1] += t*k
                t = s_str.pop() 
            else:
                t += s[i]
        return t