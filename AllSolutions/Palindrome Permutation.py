"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
Hint:

Consider the palindromes of odd vs even length. What difference do you notice?
Count the frequency of each character.
If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?
"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_counts = collections.defaultdict(int)
        for char in s:
            char_counts[char] += 1
        
        odd_char = 0
        for count in char_counts.values():
            if count %2 == 1:
                odd_char += 1
                if odd_char >1:
                    return False        
        return True 