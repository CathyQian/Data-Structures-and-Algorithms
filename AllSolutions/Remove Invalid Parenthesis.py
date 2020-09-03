"""
Remove the minimum number of invalid parentheses in order to make the input string valid. 
Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

# ref: https://yucoding.blogspot.com/2017/01/leetcode-question-remove-invalid.html

# Solution 1: BFS

""" Good explanation here
First of all, notice that the problem requires all possible results, thus a search algorithm (BFS, or DFS) often would be a good option.

Considering the BFS solution, in this problem we will expand a "tree" with all its child nodes from one level to the other, until we 
find the leaf nodes we want. So given a string s, the mimimum number of deletion is 0, which is the string itself, also it is the root
 node of our tree. If it is a valid string, we're done.

Then we expand the tree by delete only 1 parentheses, each child node is one string where 1 parentheses is deleted from the root. Therefore, 
nodes in this level of tree, represents all possible strings where only 1 parentheses is removed.

We could check each new string and see if it is a valid one. If in current level there is at lease one valid string, the search is terminated 
after this level is done. Since the minimum of deletion is current level depth, while the possible valid string are all in this level.

For the implementation, we should have:

A function to check if the string is valid or not.
A queue for the BFS, which stores the nodes in the same level.
Here I use a "map" which we will eliminate the duplicate strings, so that the number of "check" could be reduced.
Please check the C++ code below for more details.
"""


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        cur = set([s]) # start with only one element in the set, need to use set (no order, no duplicates)
        while cur:
            nxt = set() # define an empty set
            while cur: # scan one specific layer
                p = cur.pop() # pop out a random element
                if self.isValid(p):
                    res.append(p)
                if not res:
                    for i in range(len(p)): # prep all combinations for the next layer
                        if p[i] in '()':
                            nxt.add(p[:i] + p[i+1:]) # add instead of append
            if res: # if found results, no need to scan later layers since it's asking to remove minimum parentheses
                return res
            else:
                cur = nxt
 
    def isValid(self, s):
        left = 0
        for c in s:
            if c == '(': left += 1
            elif c == ')': left -= 1
            if left < 0: return False
        return left == 0


# solution 2: DFS
""" Good explanation here
Some will notice that in the BFS solution above, the bottleneck is the number of calls for "check". Each time we
 have to check all the nodes in current level and then go to next level. Alternatively, we could try using DFS.

To reduce the number of "check" being called, we could store the state (true or false) of nodes in each search
 path. So in next search if we go to the same node, we already have the states, which we don't have to check again.

Also, we could firstly compute the number of '(' and ')' to be removed by counting the parentheses in original 
string. Notice that after the removal, we still have to check the result string again.
"""

class Solution(object):
    def check(self, s):
        c = 0
        for ch in s:
            if ch == '(':
                c += 1
            if ch == ')':
                c -= 1
                if c < 0:
                    return False
        return c == 0
        
            
    def dfs(self, s, d_l, d_r, res, hist):
        if d_l == 0 and d_r == 0 : # once found, exit the dfs loop, to gurantee the minimum truncation
           if not s in res and self.check(s):
                res[s] = True
        elif s == "":
            return
        else:
            for i in range(len(s)):
                if not s[0:i] + s[i+1:] in hist:
                    hist[s[0:i] + s[i+1:]] = True
                    
                    if s[i] == '(' and d_l > 0:
                        self.dfs(s[0:i] + s[i+1:], d_l-1, d_r, res, hist)
                        
                    if s[i] == ')' and d_r > 0:
                        self.dfs(s[0:i] + s[i+1:], d_l, d_r-1, res, hist)
                        
                    
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
    
        res = {}
        hist = {}
        d_r = 0 # number of '(' to be deleted
        d_l = 0 # number of ')' to be deleted
        for ch in s:
            if ch == '(':
                d_l += 1
            if ch == ')':
                if d_l > 0:
                    d_l -= 1
                else:
                    d_r += 1
                    
                    
        self.dfs(s, d_l, d_r, res, hist)
        
        return res.keys()