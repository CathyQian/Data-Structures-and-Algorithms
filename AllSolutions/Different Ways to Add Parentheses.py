"""
Given a string of numbers and operators, return all possible results from computing all the different 
possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

"""
# Solution: divide and conquer
# scan for operators, divide between left and right, get left result and right result recursively
# combine left and right result via the operator to get the results
# be familiar with two Python function: enumerate and eval 

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        for i, char in enumerate(input):
            if char in "+-*":
                part1 = self.diffWaysToCompute(input[:i])
                part2 = self.diffWaysToCompute(input[i + 1:])
                for x in part1:
                    res += [eval(str(x) + char + str(y)) for y in part2]
        if len(res) == 0:
            res.append(eval(input))
        return res