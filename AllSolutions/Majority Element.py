"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

# Hashmap, time and space complexity both O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dic = collections.defaultdict(int)
        for n in nums:
            count_dic[n] += 1
            if count_dic[n] > len(nums)//2:
                return n

# Boyer-Moore Majority Voting Algorithm (or Moore Voting), linear time and space
"""
The Boyer-Moore majority vote algorithm is an algorithm for finding the majority of a sequence of elements
 using linear time and constant space. It is named after Robert S. Boyer and J Strother Moore, who published
 it in 1981, and is a prototypical example of a streaming algorithm.

 Idea

The idea is that we use two additional variables:

    candidate: to keep track of the potential candidate at each step.
    counter: the number of appearance of the candidate at that step.

Initially, the current candidate is None and the counter is 0. As we iterate the array over an element e, we will do the following check:

    If the counter is 0, we set the current element e as the new candidate.
    If the counter is not 0, we will check:
    If the current element e is the same as the candidate, we increment the counter by 1
    Else we decrement the counter by 1
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        V = [None, 0]
        for num in nums:
            if V[1] == 0:
                V = [num, 1]
            elif num == V[0]:
                V[1] += 1
            else:
                V[1] -= 1
        return V[0] 
                