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
        # time complexity: O(nk2)
        res = []
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                pre, post = word[:j], word[j:]
                # pre - post - pre[::-1]
                # post cannot be empty, prefix can be empty # word 1 longer than word 2
                if post and post == post[::-1] and pre[::-1] in lookup:
                    res.append([i, lookup[pre[::-1]]])
                # post[::-1] - pre - post 
                # post and pre can be both empty # word 1 shorter or equal to word 2
                if post[::-1] in lookup and pre == pre[::-1] and lookup[post[::-1]] != i:
                    res.append([lookup[post[::-1]], i])

        return res
