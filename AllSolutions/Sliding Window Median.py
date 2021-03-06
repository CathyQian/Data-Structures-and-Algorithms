"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note: 
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
"""

"""
Solution1: use two heaps, one max heap, one min heap
for every movement of the window, find the position of the removed elements, then decide what to do 
about the two heap (heap may be the best option here given that is involves frequent adding and removal of elements.
problem: need to find which element to delete each time

Solution2: maintain a sorted array including the window elements and update the array via removal and adding elements one by one

"""
# insertion sort
# time complexity: O((n-k+1)*logk), space complexity: O(k)

class Solution:
  def medianSlidingWindow(self, nums, k):
    if k == 0: return []
    ans = []
    window = sorted(nums[0:k])
    for i in range(k, len(nums)):
      ans.append((window[k // 2] + window[(k - 1) // 2]) / 2.0) # concise!
      index = bisect.bisect_left(window, nums[i - k])
      window.pop(index)      
      bisect.insort_left(window, nums[i])
    return ans
