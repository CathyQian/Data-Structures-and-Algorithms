"""
Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"

 

Constraints:

    1 <= s.length <= 10^5
    s[i] is one of  '(' , ')' and lowercase English letters.

"""

# My first thought is to use bfs to find minimum path. However, time exceed limit
# bfs solution
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s
        q = [s]
        visited = set([s])
        while q:
            ele = q.pop(0)
            if self.isValid(ele):
                return ele
            else:
                for i in range(len(ele)):
                    new = ele[:i] + ele[i+1:]
                    if new not in visited:
                        q.append(new)
                        visited.add(new)
                    if self.isValid(new):
                        return new
        return ''
    
    def isValid(self, s):
        count = 0
        for ss in s:
            if ss == '(':
                count += 1
            elif ss == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

# the right solution
# Time complexity: O(n), Space complexity: O(1)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        close = s.count(')')
        open = 0
        ans = ''
        for c in s:
            if c == '(':
                if open == close:
                    continue
                open += 1
            elif c == ')':
                close -= 1
                if open == 0:
                    continue
                open -= 1
            
            ans += c
        return ans
