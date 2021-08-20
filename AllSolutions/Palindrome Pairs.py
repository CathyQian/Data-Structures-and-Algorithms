"""
Palindrome Pairs

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]

 

Constraints:

    1 <= words.length <= 5000
    0 <= words[i].length <= 300
    words[i] consists of lower-case English letters.

"""
# time complexity O(n*k2) n == len(words), k = max(len(w) for w in words)
# https://leetcode.com/problems/palindrome-pairs/solution/
# follow up to speed lookup is to use trie to store reversed words
# start to use trie for search and don't need the second for loop
# time complexity is still O(n*k2) as building a trie takes O(n*k2)

# space complexity: lookup --- O(nk), res --- O(n2), pre/pos = O(k2)
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        lookup = {word: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            for j in range(len(word)+1): # j from 0 to len(word)
                pre, pos = word[:j], word[j:]
                # pre can be ''
                if pre == pre[::-1] and pos[::-1] != word and pos[::-1] in lookup:
                    res.append([lookup[pos[::-1]], i])
                # pos cannot be ''; otherwise will create duplicates
                if pos and pos == pos[::-1] and pre[::-1] != word and pre[::-1] in lookup:
                    res.append([i, lookup[pre[::-1]]])
        return res
