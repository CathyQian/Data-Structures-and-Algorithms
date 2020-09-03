"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""
# Solution: Dynamic Programming, O(n) time and O(n) space
"""
Since every number can only be divided by 2,3,5, one way to look at the sequence is
to split the sequence into three groups and then sort:
1) 1x2, 2x2, 3x2, 5x2,...
2) 1x3, 2x3, 3x3, 5x3,...
3) 1x5, 2x5, 3x5, 5x5

DP: array ugly for ugly numbers 
1) initialize ugly = [1]
2) Initialize three array index variables i2, i3, i5 to point to 
   1st element of the ugly array: 
        i2 = i3 = i5 = 0; 
3) from ugly[n-1] to ugly[n]
Initialize 3 choices for the next ugly no:
         L2 = ugly[i2]*2;
         L3 = ugly[i3]*3
         L5 = ugly[i5]*5;
ugly[n] = min(L2, L3, L5)
related i ++
"""

"""
Simple method is to iterate each integer and test whether they are ugly number.
The problem is the ugly numbers get really sparse as they grow bigger, which makes
the search very slow.
"""
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0

        while len(ugly) < n:
            L2, L3, L5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
            m = min(L2, L3, L5)
            if m == L2:
                i2 += 1
            if m == L3: # not elif
                i3 += 1 # not elif
            if m == L5:
                i5 += 1

            ugly.append(m)

        return ugly[-1]






