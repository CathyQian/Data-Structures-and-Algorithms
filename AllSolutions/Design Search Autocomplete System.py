"""
Design Search Autocomplete System

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:

    The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
    The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
    If less than 3 hot sentences exist, return as many as you can.
    When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

Implement the AutocompleteSystem class:

    AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
    List<String> input(char c) This indicates that the user typed the character c.
        Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
        Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than 3 matches, return them all.

 

Example 1:

Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

Explanation
AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
obj.input("a"); // return []. There are no sentences that have prefix "i a".
obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

 

Constraints:

    n == sentences.length
    n == times.length
    1 <= n <= 100
    1 <= sentences[i].length <= 100
    1 <= times[i] <= 50
    c is a lowercase English letter, a hash '#', or space ' '.
    Each tested sentence will be a sequence of characters c that end with the character '#'.
    Each tested sentence will have a length in the range [1, 200].
    The words in each input sentence are separated by single spaces.
    At most 5000 calls will be made to input.

"""

# solution using trie and dfs
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        # define a trie to store the sentences
        self.root = {}
        self.cur_input = ''
        for i, sentence in enumerate(sentences):
            self.addSentence(sentence, times[i])
        self.curnode = self.root
        self.is_preSuccess = True
        
    def addSentence(self, sentence, count):
        # add sentence to the trie
        node = self.root
        for ch in sentence:
            if ch not in node:
                node[ch] = {}
            node = node[ch] # pay attention to indendation
        # add count to the end of the sentence
        if '*' in node:
            node['*'][0] += count
        else:
            node['*'] = [count, sentence]
        
    def findTop3Sentence(self, ch):
        # find Top3 sentences starting with ch and start from self.cur_node
        res = []
        if self.is_preSuccess == False or ch not in self.curnode.keys():
            self.is_preSuccess = False # important
            return res
        else:  
            self.curnode = self.curnode[ch]
            self.dfs(self.curnode, res) # dfs in trie, important
            if res:
                self.is_preSuccess = True
                res.sort(key = lambda x: (-x[0], x[1]), reverse =False) # sort by two standard

            return [x[1] for x in res[:3]]
    
    def dfs(self, node, res):
        # find all sentences and put in res starting from node
        if '*' in node:
            res.append(node['*'])
        for c in node:
            if c != '*':
                self.dfs(node[c], res)
            
    def input(self, c: str) -> List[str]:
        # input c and return top 3 sentences in order
        if c == '#': # end of a sentence
            self.addSentence(self.cur_input, 1)
            self.cur_input = ''
            self.curnode = self.root
            self.is_preSuccess = True
            return []
        else:
            self.cur_input += c
            return self.findTop3Sentence(c)
            
    
            
           
            

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)