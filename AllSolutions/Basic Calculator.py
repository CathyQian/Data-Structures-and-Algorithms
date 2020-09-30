"""
Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2

Example 2:

Input: " 2-1 + 2 "
Output: 3

Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:

    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.


"""

# do everything in one path, only append elements to stack if '('
class Solution:
    def calculate(self, s: str) -> int:
        res, sign = 0, 1
        n = len(s)
        stack = []
        i = 0 
        while i < len(s):
            if s[i].isnumeric():
                num = 0
                while i < n and s[i].isnumeric():
                    num = 10 * num + int(s[i])
                    i += 1
                res += sign * num
                i -= 1
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif s[i] == ')':
                res *= stack.pop(-1)
                res += stack.pop(-1)
            i += 1
        return res