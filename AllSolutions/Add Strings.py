"""
Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.


"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        if len(num1) < len(num2):
            num1, num2 = num2, num1 
        i = len(num2) - 1
        j = len(num1) - len(num2)
        mod = 0 
        while i >= 0:
            mod, residual = divmod(int(num1[i+j]) + int(num2[i]) + mod, 10)
            res += str(residual)
            i -= 1
        j -= 1
        while j >= 0:
            mod, residual = divmod(int(num1[j]) + mod, 10)
            res += str(residual)
            j -= 1
        if mod > 0:
            res += str(mod)
        return res[::-1]