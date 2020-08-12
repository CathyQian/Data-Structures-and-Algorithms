"""
Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

"""
# method 1, brutal force, time complexity O(n3), space complexity O(n)
# time exceed limit in Leetcode
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxlen = 0
        for i in range(len(s)-1):
            for j in range(i+2, len(s)+1):
                if self.isValid(s[i:j]):
                    maxlen = max(maxlen, j-i)
        return maxlen
    
    def isValid(self, s):
        stack = []
        for k in range(len(s)):
            if s[k] == '(':
                stack.append(s[k])
            else:
                if stack and stack[-1] == '(': # not if stack[-1], since stack may be empty here
                    stack.pop(-1)
                else:
                    return False
        return True if not stack else False
                    
        
# method 2, use stack, time O(n), space complexity O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxlen = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop(-1)
                if not stack:
                    stack.append(i)
                else:
                    maxlen = max(maxlen, i - stack[-1])
        return maxlen

# Two other methods: using DP or dural pointer: https://leetcode.com/problems/longest-valid-parentheses/solution/