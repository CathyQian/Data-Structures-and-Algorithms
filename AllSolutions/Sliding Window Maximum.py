"""
Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]

Example 4:

Input: nums = [9,11], k = 2
Output: [11]

Example 5:

Input: nums = [4,-2], k = 2
Output: [4]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    1 <= k <= nums.length

"""

# time complexity ~ O(N), space complexity ~ O(N)
# Solution: keep an array with index of elements, these elements are in descending order
# for new elements, pop out any elements smaller than it before adding the new element; check if the biggest element needs to be popped out, if yes --> do it
# the biggest element is always the first element in the array after above processing
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: 
        res = []
        q = deque()
        for i in range(len(nums)):
            # pop out left element if index is correct; otherwise do nothing
            if q and q[0] == i - k:
                _ = q.popleft()
            # add new element, pop out anyone smaller than it before adding
            while q and nums[q[-1]] < nums[i]:
                _ = q.pop()
            q.append(i)
            # add max to res
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
