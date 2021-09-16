"""
Shortest Word Distance III

Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.


Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1

Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
Output: 3

 

Constraints:

    1 <= wordsDict.length <= 105
    1 <= wordsDict[i].length <= 10
    wordsDict[i] consists of lowercase English letters.
    word1 and word2 are in wordsDict.



"""

#O(n) time O(1) space:

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):   
        n = len(words)
        minimum = n
        w1 = -1
        w2 = -1
        for i in range(n):
            if words[i] == word1:
                w1 = i
                if w2 != -1:
                    minimum = min(w1-w2,minimum)
            if words[i] == word2:
                w2 = i
                if w1 != -1 and w1 != w2:
                    minimum = min(w2-w1,minimum)
        return minimum

# Solution for shortest word distance II (such search happens many times)
import collections
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word2index = collections.defaultdict(list)
        for idx, word in enumerate(wordsDict):
            self.word2index[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        index1 = self.word2index[word1]
        index2 = self.word2index[word2]
        i, j = 0, 0
        mindist = sys.maxsize
        while i < len(index1) and j < len(index2):
            mindist = min(mindist, abs(index1[i]-index2[j]))
            if index1[i] > index2[j]:
                j += 1
            elif index1[i] < index2[j]:
                i +=1
        return mindist