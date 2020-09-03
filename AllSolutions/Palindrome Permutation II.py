"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].

Hint:

If a palindromic permutation exists, we just need to generate the first half of the string.
To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.
"""

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
                if odd_count >1:
                    return []
         
        half_permu = [] 
        self.dfs('', half_permu, even_chars)
        result = []
        for s in half_permu:
            result.append(s+mid_char+s[::-1])
        return result
    
    def dfs(self, base, half_permu, even_chars):
        if not even_chars:
            half_permu.append(base)
        curr=''
        for idx in range(len(even_chars)):
            if even_chars[idx] == curr:
                continue
            else:
                curr= even_chars[idx]
                self.dfs(base+curr, half_permu, even_chars[:idx]+even_chars[idx+1:])s