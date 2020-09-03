"""
Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

"""

"""
这道题最大的难点，就是对于星号的处理，可以匹配任意字符串，简直像开了挂一样，就是说在星号对应位置之前，
不管你s中有任何字符串，我大星号都能匹配你，主角光环啊。但即便叼如斯的星号，也有其处理不了的问题，那就
是一旦p中有s中不存在的字符，那么一定无法匹配，因为星号只能增加字符，不能消除字符，再有就是星号一旦确
定了要匹配的字符串，对于星号位置后面的匹配情况也就鞭长莫及了 (if multiple * is found and mismatch is 
found after the second *, don't rematch from the first * since it won't be able to correct the 
mismatch regardless. Therefore, jStar will only move forward. iStar also only moves forward as
multiple matches can be done with one *)。所以p串中星号的位置很重要，用 jStar 来
表示，还有星号匹配到s串中的位置，使用 iStart 来表示，这里 iStar 和 jStar 均初始化为 -1，表示默认情
况下是没有星号的。然后再用两个变量i和j分别指向当前s串和p串中遍历到的位置。

开始进行匹配，若i小于s串的长度，进行 while 循环。若当前两个字符相等，或着p中的字符是问号，则i和j分别
加1。若 p[j] 是星号，要记录星号的位置，jStar 赋为j，此时j再自增1，iStar 赋为i。若当前 p[j] 不是星号，
并且不能跟 p[i] 匹配上，此时就要靠星号了，若之前星号没出现过，那么就直接跪，比如 s = "aa" 和 p = "c*"，
此时 s[0] 和 p[0] 无法匹配，虽然 p[1] 是星号，但还是跪。如果星号之前出现过，可以强行续一波命，比如 
s = "aa" 和 p = "*c"，当发现 s[1] 和 p[1] 无法匹配时，但是好在之前 p[0] 出现了星号，把 s[1] 交给 
p[0] 的星号去匹配。至于如何知道之前有没有星号，这时就能看出 iStar 的作用了，因为其初始化为 -1，而遇到
星号时，其就会被更新为i，只要检测 iStar 的值，就能知道是否可以使用星号续命。虽然成功续了命，匹配完了s
中的所有字符，但是之后还要检查p串，此时没匹配完的p串里只能剩星号，
不能有其他的字符，将连续的星号过滤掉，如果j不等于p的长度，则返回 false
"""

"""
string p and s needs to be fully matched without residual in both strings.
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j, iStar, jStar = 0, 0, -1, -1
        m, n = len(s), len(p)
        while i < m:
            if j < n and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                iStar = i
                jStar = j
                j += 1
            elif iStar >= 0:# if there is previous * in p, use * to match s
                iStar += 1 # iStar moves forward everytime a match is done, may be matched multiple times
                i = iStar
                j = jStar + 1 # jStar don't move over time, unless a new * is found
            else:
                return False
             
        while j<n and p[j] == '*':
            j += 1
        return j == n
                