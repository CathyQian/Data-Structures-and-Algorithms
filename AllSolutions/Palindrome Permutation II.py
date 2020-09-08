"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].

Hint:

If a palindromic permutation exists, we just need to generate the first half of the string.
To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.
"""
# dfs + trick in permutation (to avoid duplicates, otherwise time exceed limit)
import collections

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        char_count = collections.defaultdict(int)
        for char in s:
            char_count[char] += 1   
        
        mid_char = ''
        even_chars = []
        odd_count = 0
        
        for char, count in char_count.items():
            if count % 2 == 0:
                even_chars += [char]*(count//2)
            else:
                mid_char = char
                odd_count += 1
                even_chars += [char]*(count//2)
                if odd_count > 1:
                    return []
        self.result = set()
        self.permute(even_chars, mid_char, [])
        return list(self.result)
    
    def permute(self, s, m, path):
        if not s: # end of the dfs
            if m:
                self.result.add(''.join(path) + m + ''.join(path[::-1]))
            else:
                self.result.add(''.join(path) + ''.join(path[::-1]))
        else:
            for i in range(len(s)):
                if i == 0 or s[i] != s[i-1]:
                     self.permute(s[:i]+s[i+1:], m, path + [s[i]])
