"""
Factor Combinations

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.

Write a function that takes an integer n and return all possible combinations of its factors.

Note:

    You may assume that n is always positive.
    Factors should be greater than 1 and less than n.

Example 1:

Input: 1
Output: []

Example 2:

Input: 37
Output:[]

Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]

Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]


"""

# not that hard, but make sure factors are changed back after each for loop (line 70)
# Time: O(nlogn) 
# Space: O(logn) # i * i < n

class Solution:
    def getFactors(self, n):        
        result = []         
        self.getResult(n, result, [])        
        return result    

    def getResult(self, n, result, factors):        
        i = 2 if not factors else factors[-1] # returning elements in increasing order      
        while i <= n / i:            
            if n % i == 0:                      
                result.append(factors + [i, n//i])
                self.getResult(n // i, result, factors + [i])        
            i += 1
        
