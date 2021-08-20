"""
Shortest Word Distance II

Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

    WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
    int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.

 

Example 1:

Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1

 

Constraints:

    1 <= wordsDict.length <= 3 * 104
    1 <= wordsDict[i].length <= 10
    wordsDict[i] consists of lowercase English letters.
    word1 and word2 are in wordsDict.
    word1 != word2
    At most 5000 calls will be made to shortest.

"""
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        
        self.word2pos = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.word2pos[word].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        
        pos1 = self.word2pos[word1]
        pos2 = self.word2pos[word2]
        mindist = sys.maxsize
        l1, l2 = 0, 0
        while l1 < len(pos1) and l2 < len(pos2):
            mindist = min(mindist, abs(pos1[l1] - pos2[l2]))
            if pos1[l1] < pos2[l2]:
                l1 += 1
            else:
                l2 += 1      
        return mindist

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

# Time, init --- O(n) n is length of wordsDict, 
# shortest ---  for the function that finds the minimum distance between the two words, the complexity would be O(k+l)) where KKK 
# and LLL represent the number of occurrences of the two words. However, K=O(N)K = O(N)K=O(N) and also
# L=O(N)L = O(N)L=O(N). Therefore, the overall time complexity would also be O(N)O(N)O(N)