"""
Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""

# make sure to optimize the solution, instead of match every time

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if m < n:
            return []
        p_count = collections.defaultdict(int)
        s_count = collections.defaultdict(int)
        for pp in p:
            p_count[pp] += 1 
        for ss in s[:n]:
            s_count[ss] += 1
        res = []
        
        if s_count == p_count:
            res.append(0)
        for i in range(n, m):
            s_count[s[i]] += 1
            s_count[s[i-n]] -= 1
            if s_count[s[i-n]] == 0:
                _ = s_count.pop(s[i-n])
            if s_count == p_count:
                res.append(i-n+1)
        return res
    