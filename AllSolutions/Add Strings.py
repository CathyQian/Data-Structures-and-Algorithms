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
        i, j = len(num1) -1 , len(num2) -1
        
        mod = 0 
        while i >= 0 or j >= 0:
            total = 0
            if i >= 0:
                total += int(num1[i])
                i -= 1
            if j >= 0:
                total += int(num2[j])
                j -= 1
            total += mod
            mod, residual = divmod(total, 10)
            res += str(residual)

        if mod > 0:
            res += str(mod)
        return res[::-1]