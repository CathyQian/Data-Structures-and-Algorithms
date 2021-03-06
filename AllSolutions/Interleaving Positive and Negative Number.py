"""
Given an array with positive and negative integers. Re-range it to interleaving with positive and negative 
integers.

You are not necessary to keep the original order of positive integers or negative integers.

Example 1

Input : [-1, -2, -3, 4, 5, 6]
Outout : [-1, 5, -2, 4, -3, 6]
Explanation :  any other reasonable answer.

Challenge

Do it in-place and without extra memory.

"""

class Solution:
    def rerange(self, A):
        # write your code here
        count = 0
        for i in range(len(A)):
            if A[i] < 0:
                A[i], A[count] = A[count], A[i]
                count += 1
        # options: if len(A) is even, count = len(A)/2, if len(A) is odd, count = (len(A)+1)/2 or (len(A)-1)/2
        if count > len(A) - count:
            l, r = 1, count*2-2
        l, r = 0, count*2 - 1 
        while l < r:
            A[l], A[r] = A[r], A[l]
            l += 2
            r -= 2
        return 
