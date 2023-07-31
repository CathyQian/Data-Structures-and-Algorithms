"""
Basic Calculator III

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open (and closing parentheses), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open (and closing parentheses) and empty spaces . The
integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12

Note: Do not use the eval built-in library function.

"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                num = 0
                while i < len(s) and s[i].isnumeric():
                    num = num*10 + int(s[i])
                    i += 1
                stack.append(num)
                i -= 1
            elif s[i] in ['+', '-', '*', '/', '(']:
                stack.append(s[i])
            elif s[i] == ')':
                new = []
                while stack and stack[-1] != '(':
                    new.append(stack.pop(-1))
                res = self.operations(new[::-1])
                if stack:
                    stack[-1] = res
                else:
                    stack.append(res)
            i += 1
        return self.operations(stack)                     
        
    def operations(self, l):
        # list of int, +, -, *, /
        stack = []
        i = 0
        while i < len(l):

            if l[i] == '*':
                stack[-1] *= l[i+1]
                i += 2
            elif l[i] == '/':
                if stack[-1] < 0:
                    stack[-1] = -(-stack[-1]//l[i+1])
                else:
                    stack[-1] //= l[i+1]
                i += 2
            elif l[i] == '-':
                stack.append(-l[i+1])
                i += 2
            elif l[i] == '+':
                stack.append(l[i+1])
                i += 2
            else:
                stack.append(l[i])
                i += 1
        return sum(stack)
    

# Time exceed limit

class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        cur, i = -1, 0
        ops = '+'
        while i < len(s):
            if s[i].isdigit():
                cur = 0
                while i < len(s) and s[i].isdigit():
                    cur = cur*10 + int(s[i])
                    i += 1
                i -= 1
            elif s[i] == '(':
                # keep going until find ')'
                start, parenthesisCnt = i, 1
                i += 1
                while i < len(s) and parenthesisCnt != 0:
                    if s[i] == '(':
                        parenthesisCnt += 1
                    elif s[i] == ')':
                        parenthesisCnt -= 1
                    i += 1
                cur = self.calculate(s[start+1:i])
            
            elif s[i] in ['*', '/', '-', '+']:
                ops = s[i]

            if cur >= 0: # non-negative
                if ops == '+':
                    nums.append(cur)
                elif ops == '-':
                    nums.append(-1*cur)
                elif ops == '*':
                    nums[-1] *= cur
                elif ops == '/':
                    nums[-1] //= cur
                ops = '+'
                cur = -1
            i += 1
            
            print(ops, cur, nums)
        return sum(nums)