"""
24 Game

You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:

Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24

Example 2:

Input: [1, 2, 1, 2]
Output: False

Note:

    The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
    Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
    You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.

"""
"""
Analysis:
Three aspects for permutation: 1) numbers --- A4-4 = 4*3*2 = 24 2) operations A4--3 = 24
3) parenthesis --- easiest one, A3-3 = 6 but actually only 5 since two can be combined.
"""

# method 1
class Solution:
    def judgePoint24(self, nums):
        if len(nums) == 1:
            return math.isclose(nums[0], 24) # cannot use == as / in python will keep limited decimal points (depending on # of bits used to represent each number)
        for a, b, *rest in itertools.permutations(nums):
            # rest is a list here
            for x in {a+b, a-b, a*b, b and a/b}:
                if self.judgePoint24([x] + rest):
                    return True
        return False

# method 2, I personally like this method best, since it considers all senarios and faster if nums has duplicates
# note method 1 and 2 permute in different ways, so method 1 doesn't need to consider brackets, but method 2 needs

import itertools
from operator import add, mul, sub # can't use truediv from operator
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def div(a, b):
            if b == 0:
                return sys.maxsize
            return a/b
        Ops = list(itertools.product([add,sub,mul,div], repeat=3))
        for ns in set(itertools.permutations(nums)):
            for ops in Ops:
                # (((W op X) op Y) op Z)
                result = ops[0](ns[0], ns[1])
                result = ops[1](result, ns[2])
                result = ops[2](result, ns[3])
                if 23.99 < result < 24.01: # math.isclose(nums[0], 24)
                    return True

                # (W op (X op Y)) op Z))
                result = ops[1](ns[1], ns[2])
                result = ops[0](ns[0], result)
                result = ops[2](result, ns[3])
                if 23.99 < result < 24.01:
                    return True
                
                # (W op (X op Y op Z))
                result = ops[1](ns[1], ns[2])
                result = ops[2](result, ns[3])
                result = ops[0](ns[0], result)
                if 23.99 < result < 24.01:
                    return True
                
                # ((W op X) op (Y op Z))
                result1 = ops[0](ns[0], ns[1])
                result2 = ops[2](ns[2], ns[3])
                result = ops[1](result1, result2)
                if 23.99 < result < 24.01:
                    return True
                
                # W op (X op (Y op Z))
                result = ops[2](ns[2], ns[3])
                result = ops[1](ns[1], result)
                result = ops[0](ns[0], result)
                if 23.99 < result < 24.01:
                    return True
        return False

"""
First I iterate all the unique permutations of the provided 4 numbers (make sure uniqueness by using a
 set).
Then as you can see from my comments, there are 4 possible situations when brackets are involved so I 
tried to check all of them in 1 for loop.
Since each operation can be repeated and exactly 3 operations need to be used, I decided to store the 
cartesian product of all the possible operation functions in a list to iterate all possibilities.

Time complexity I believe is: 64 * 12 * 24 => O(1)
"""


# method 3, dfs, this is incorrect as it's only considering the first and third op, excluding the second op
from fractions import Fraction
from operator import add, sub, mul, truediv

class Solution:
    def judgePoint24(self, nums):
        def dfs(nums):         
            if len(nums) == 1:             
                return nums[0] == 24 
            x = nums.pop(0)         
            y = nums.pop(0) 
            res = False         
            for op in [add, sub, mul, truediv]:             
                if op in [add, mul]:                 
                    res = res or dfs([op(x, y)] + nums) 
                elif op == sub:                 
                    res = res or dfs([op(x, y)] + nums)
                    res = res or dfs([op(y, x)] + nums)
                else:                 
                    if y != 0:                     
                        res = res or dfs([op(x, y)] + nums) 
                    if x != 0:                     
                        res = res or dfs([op(y, x)] + nums)
            return res     
        
        return dfs([Fraction(num) for num in nums])
