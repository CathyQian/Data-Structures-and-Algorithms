"""
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

"""

# recursion, make sure dictionary key is string, not integer
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'} 
        if len(digits) == 0:
            return []
        result = []
        res = self.letterCombinations(digits[1:])
        for l in dic[digits[0]]:
            if res:
                for r in res:
                    result.append(l + r)
            else:
                result.append(l)
        return result
        
# dfs
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.dic = {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'}
        res = []
        self.dfs(digits, 0, '', res)
        return res
    
    def dfs(self, digits, start, path, res):
        if start == len(digits):
            if path != '':
                res.append(path)

        else:
            for e in self.dic[digits[start]]:
                self.dfs(digits, start+1, path + e, res)
  
# time complexity O(n*4**n), n is len(digits)
# reason: There are ultimately 4^N combinations (worst case) of strings generated, and for each of 
# those combinations you have to actually construct the string.
# Constructing a string of N length is an O(N) operation. So thus 4^N * N.
# space complexity:hashmap ---O(1),  O(N*4**N) for output size, O(N) for parameters in dfs
