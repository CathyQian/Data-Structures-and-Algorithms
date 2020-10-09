Everything about String to Calculators

- [Basic Calculator I](AllSolutions/Basic%20Calculator.py) (**)
- [Basic Calculator II](AllSolutions/Basic%20Calculator%20II.py) (**)
- [Basic Calculator III](AllSolutions/Basic%20Calculator%20III.py) (**)
- [Decode String](/AllSolutions/Decode%20String.py)

"""
two-steps method:
- define operator function to calculate operations without parenthesis
- read the input string as a list into a stack, user operators when come across parenthesis
- return operator(stack) if stack not empty
"""
```Python
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
                if stack: # important
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
                i += 1 
            else:
                stack.append(l[i])
                i += 1
        return sum(stack)

```
- [Decode String](/AllSolutions/Decode%20String.py)

```Python
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
```

- **[Different Ways to Add Parentheses](AllSolutions/Different%20Ways%20to%20Add%20Parentheses.py) (divide and conquer)

- **[Expression Add Operators](AllSolutions/Expression%20Add%20Operators.py)
```Python
# the key point here when there is * or /, you need to remember both the previous elements and the previous sign
# solution is typical dfs for path finding
# can't use memo here

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.ans = []
        self.dfs(num, target, 0, "", 0, 0)
        return self.ans

    def dfs(self, num, target, pos, exp, prev, curr):
        if pos == len(num):
            if curr == target: 
                self.ans.append(exp)
            return

        for l in range(1, len(num) - pos + 1):
            t = num[pos: pos+l] # next element for operation   
            if t[0] == '0' and len(t) > 1: # edge case 1
                break

            if pos == 0: # edge case 2
                self.dfs(num, target, l, t, int(t), int(t))
                continue

            self.dfs(num, target, pos + l, exp + '+' + t, int(t), curr + int(t))
            self.dfs(num, target, pos + l, exp + '-' + t, -int(t), curr - int(t))
            self.dfs(num, target, pos + l, exp + '*' + t, prev * int(t), curr - prev + prev * int(t))

```