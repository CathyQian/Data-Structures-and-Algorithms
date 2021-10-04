"""
Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

 

Constraints:

    1 <= word.length <= 500
    word in addWord consists lower-case English letters.
    word in search consist of  '.' or lower-case English letters.
    At most 50000 calls will be made to addWord and search.


"""
# dfs + trie
# need to ask if '.' can represent empty space or only any ONE letter
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.words = set()
        
    def addWord(self, word: str) -> None: # O(len(word))
        """
        Adds a word into the data structure.
        """
        if word not in self.words:
            self.words.add(word)
            node = self.root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['*'] = word        

    def search(self, word: str) -> bool: # O(len(word))
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if '.' not in word:
            if word in self.words:
                return True
            else:
                return False
        return self.searchWord(self.root, word)
    
    def searchWord(self, node, word):
        for i, ch in enumerate(word):
            if ch != '.' and ch not in node:
                return False
            elif ch != '.' and ch in node:
                node = node[ch]
            elif ch == '.':
                for key in node:
                    if key != '*' and self.searchWord(node[key], word[i+1:]):
                        return True
                return False # key step, easy to ignore
            
        if '*' in node: # also easy to ignore
            return True
        
        return False

    
# another solution, easier to implement    
# n: number of words, m: avg length of words ----> search O(mn)
class WordDictionary:

    def __init__(self):
        self.len2words = collections.defaultdict(set)
        self.words_set = set()

    def addWord(self, word: str) -> None:
        self.words_set.add(word)
        self.len2words[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        if '.' not in word:
            if word in self.words_set:
                return True
            else:
                return False
            
        else:
            if len(word) not in self.len2words:
                return False
            candidates = self.len2words[len(word)]
            for candidate in candidates:
                i = 0
                while i < len(word):
                    if word[i] == '.' or word[i] == candidate[i]:
                        i += 1
                    else:
                        break
                if i == len(word):
                    return True
            return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
