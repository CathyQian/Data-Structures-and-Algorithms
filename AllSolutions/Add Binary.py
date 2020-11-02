"""
Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

 

Constraints:

    Each string consists only of '0' or '1' characters.
    1 <= a.length, b.length <= 10^4
    Each string is either "0" or doesn't contain any leading zero.

"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        flag = 0
        res = ''
        i, j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0:
            total = 0
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            total += flag
            if total == 3:
                res += '1'
                flag = 1
            elif total == 2:
                res += '0'
                flag = 1
            else:
                res += str(total)
                flag = 0
        if flag == 1:
            res += '1'
        return res[::-1]