"""
[227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

Example 2:

Input: " 3/2 "
Output: 1

Example 3:

Input: " 3+5 / 2 "
Output: 5

Note:

    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num, operation = 0, '+'
        operations = set({'*', '+', '/', '-'})
        for ch in s+'+':
            if ch.isdigit():
                num = num*10 + int(ch) 
            elif ch in operations:
                if operation == '/': 
                    stack[-1] = int(stack[-1]/num)
                elif operation == '*': stack[-1] = stack[-1]*num
                else:
                    if operation == '-': num = -num
                    stack.append(num)
                    
                num, operation = 0, ch
                
        return sum(stack)
        
# easier to understand solution, time O(n)

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ops = '+'
        i = 0 
        while i < len(s):
            if s[i].isnumeric():
                num = 0
                while i < len(s) and s[i].isnumeric():
                    num = 10 * num + int(s[i])
                    i += 1
                if ops == '*':
                    stack[-1] *= num
                elif ops == '/': # a bit tricky here
                    if stack[-1] < 0:
                        stack[-1] = -(-stack[-1]//num)
                    else:
                        stack[-1] = stack[-1]//num
                elif ops == '+':
                    stack.append(num)
                elif ops == '-':
                    stack.append(-num)
                i -= 1
            elif s[i] in ['*', '/', '+', '-']:
                ops = s[i]    
            i += 1
        return sum(stack)
        