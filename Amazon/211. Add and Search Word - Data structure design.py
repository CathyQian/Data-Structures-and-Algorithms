"""
[211. Add and Search Word - Data structure design](https://leetcode.com/problems/add-and-search-word-data-structure-design/)

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.

"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = collections.defaultdict(list)
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.words[len(word)].append(word)
   
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if len(word) not in self.words:
            return False
        cur = self.words[len(word)]
        for w in cur:
            res = True
            for i in range(len(w)):
                if w[i] == word[i] or word[i] == '.':
                    pass
                else:
                    res = False
                    break
            if res:
                return True
        return False