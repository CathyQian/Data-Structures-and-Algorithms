"""
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

    0 <= i < j < nums.length
    nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

Example 2:

Input: nums = [13,10,35,24,76]
Output: 4

 
"""


# time complexity O(n2), time limit exceed
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + self.rev(nums[j]) == nums[j] + self.rev(nums[i]):
                    count += 1
        return count
    
    def rev(self, n):
        return int(str(n)[::-1])
    
    
# correct solution
    
"""
Please note following observations which helped to simplify the thought process while solving the question
    0 <= i < j < nums.length -> This condition doesn't have signifiance, as we're dealing with + operator which is 
    associative in nature
    nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]) -> This can be re-written as nums[i]-rev(nums[i]) == 
    nums[j]-rev(nums[j]) i.e. diff(nums[i]) == diff(nums[j]) 
    where diff(anyNum) is defines as nums[anyNum]-rev(nums[anyNum]

Hence, the problem boils down to sort the input array as considering diff as "comparison key". And, then we just need
to count the frequencies corresponding to each diff and add the number of pairs which can be chosen corresponding to
each frequency.

ref: https://leetcode.com/problems/count-nice-pairs-in-an-array/discuss/1140577/Accepted-Python-simple-and-easy-to-understand-solution-with-comments
"""
import collections
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        # define constants
        n = len(nums)
        MOD = 10**9 + 7
        
        # handle scenario for no pairs
        if n <= 1:
            return 0
        
        # utility method to calculate reverse of a number
        # e.g. rev(123) -> 321
        def rev(n):
            return int(str(n)[::-1])
        
        # calculate frequency of all the diffs
        freq_counter = collections.defaultdict(int)
        for num in nums:
            freq_counter[num-rev(num)] += 1
        
        # for all the frequencies calculate the number of paris
        # which is basically nC2 (read as - "n choose 2") -> n*(n-1)/2
        answer = 0
        for key, count in freq_counter.items():
            answer = (answer + (count*(count-1))//2)%MOD
                          
        return answer
                
