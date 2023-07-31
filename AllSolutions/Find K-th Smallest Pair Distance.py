"""
Find K-th Smallest Pair Distance

The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5
 

Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
"""

# method 1: brutal force, memory limit exceeded
import heapq
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # n(n-1)/2 pairs, brutal force, get all pairs, put in heap, get nsmallest(k)
        distances = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                distances.append(abs(nums[j] - nums[i]))
        heapq.heapify(distances)
        return heapq.nsmallest(k, distances)[-1]

# method 2: brutal force with modified heap, time limit exceeded
import heapq
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # n(n-1)/2 pairs, brutal force, get all pairs, put in heap, get nsmallest(k)
        if not nums or k <= 0:
            return None
        distances = []  # max len is k
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if len(distances) < k:
                    distances.append(- abs(nums[j] - nums[i]))
                    if len(distances) == k:
                        heapq.heapify(distances)
                else: # len(distances) == k
                    if - abs(nums[j] - nums[i]) > distances[-1]:
                        heapq.heappop(distances)
                        heapq.heappush(distances, -abs(nums[j] - nums[i]))
        return -distances[0]

# method 3: binary search
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        
        while left <= right: # use binary search to find the correct distance 
            mid = left + (right - left) // 2
            start = 0
            count = 0
            
            # how many pairs' distance <= mid
            for i in range(n):
                while nums[i] - nums[start] > mid:
                    start += 1
                count += i - start
            # critical    
            if count < k:
                left = mid + 1
            else:
                right = mid - 1 
        
        return left