"""
Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

    Only one letter can be changed at a time
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

    Return an empty list if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        layer = {beginWord:[[beginWord]]}
        while layer:
            new_layer = collections.defaultdict(list)
            visited = set()
            for word in layer:
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        new = word[:i] + j + word[i+1:]
                        if new != word and new in wordList:
                            new_layer[new] += [l+[new] for l in layer[word]] # don't use append here as append returns None
                            visited.add(new)
            if endWord in new_layer:
                 return new_layer[endWord]
            wordList -= visited
            layer = new_layer
        return []