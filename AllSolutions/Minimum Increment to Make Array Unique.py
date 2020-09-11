"""
Minimum Increment to Make Array Unique

Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].

Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

 

Note:

    0 <= A.length <= 40000
    0 <= A[i] < 40000
"""

# brutal force, time exceed limit
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A_set = set()
        moves = 0
        for a in A:
            while a in A_set:
                a += 1
                moves += 1
            A_set.add(a)
        return moves
       
 # sort A first     
 class Solution:
     def minIncrementForUnique(self, A: List[int]) -> int:
         A.sort()
         need, res = 0, 0
         for a in A:
             res += max(need-a, 0)
             need = max(need, a) + 1
         return res
        
# what if there are lots of duplicates? use hashmap and ordered dict
import collections
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        res, need = 0, 0
        numCnt = collections.OrderedDict()
        for a in A:
            if a not in numCnt:
                numCnt[a] = 1
            else:
                numCnt[a] += 1
        while numCnt:
            num, count = numCnt.popitem(last=False)
            res += max((need - num)*count, 0) + count*(count-1)//2
            need = max(num, need) + count
            
        return res
