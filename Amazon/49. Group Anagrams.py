"""
[Leetcode](https://leetcode.com/problems/group-anagrams/)

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.


"""
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for i, s in enumerate(strs):
            s = ''.join(sorted(s)) # sorted(s) becomes a list
            dic[s].append(strs[i])
        return dic.values()