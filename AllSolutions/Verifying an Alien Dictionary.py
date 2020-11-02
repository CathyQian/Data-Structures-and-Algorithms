"""
Verifying an Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.


"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {' ': -1}
        rank = 0
        for s in order:
            order_dict[s] = rank
            rank += 1
        for w1, w2 in list(zip(words, words[1:])):
            w1 += ' '
            w2 += ' '
            i = 0
            while i < len(w1) and i < len(w2):
                if w1[i] == w2[i]:
                    i += 1
                else:
                    idx1 = order_dict[w1[i]]
                    idx2 = order_dict[w2[i]]
                    if idx1 > idx2:
                        return False
                    else:
                        break
        return True