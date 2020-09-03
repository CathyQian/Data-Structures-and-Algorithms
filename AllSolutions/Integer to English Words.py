"""
Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"

Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

"""

class Solution:

    def numberToWords(self, num: int) -> str:
        self.mp = {1: "One",   11: "Eleven",    10: "Ten", 
                   2: "Two",   12: "Twelve",    20: "Twenty", 
                   3: "Three", 13: "Thirteen",  30: "Thirty", 
                   4: "Four",  14: "Fourteen",  40: "Forty",
                   5: "Five",  15: "Fifteen",   50: "Fifty", 
                   6: "Six",   16: "Sixteen",   60: "Sixty", 
                   7: "Seven", 17: "Seventeen", 70: "Seventy", 
                   8: "Eight", 18: "Eighteen",  80: "Eighty",
                   9: "Nine",  19: "Nineteen",  90: "Ninety"}
        
        ans = []
        for i, unit in zip((9, 6, 3, 0), ("Billion", "Million", "Thousand", "")): 
            n, num = divmod(num, 10**i)
            ans.extend(self.fn(n))
            if n and unit: 
                ans.append(unit)
                
        return "Zero" if not ans else " ".join(ans)
    
    def fn(self, n):
        """Return English words of n (0-999) in array."""
        if not n: 
            return []
        elif n < 20: 
            return [self.mp[n]]
        elif n < 100: 
            return [self.mp[n//10*10]] + self.fn(n%10)
        else: 
            return [self.mp[n//100], "Hundred"] + self.fn(n%100)