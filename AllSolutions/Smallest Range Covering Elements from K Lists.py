"""
Smallest Range Covering Elements from K Lists
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
 

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.

"""
# list solution
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # build a minheap, pop len(nums) elements, if index from 0 to len(nums), get gap, record min, max and gap; iterate and find mingap, return min and max
        h = []
        # initialization: put the first element in 
        for i in range(len(nums)):
            h.append((nums[i][0], (i, 0)))
        h.sort()
  
        # initialization
        minval, (min_i, min_j) = h[0]
        maxval, (max_i, max_j) = h[-1]
        gap = maxval - minval

        # scan across all nums
        while len(h) == len(nums):
            _, (min_i, min_j) = h.pop(0)
            if min_j < len(nums[min_i]) - 1:
                bisect.insort_right(h, (nums[min_i][min_j + 1], (min_i, min_j + 1)))
            else:
                break
            if h[-1][0] - h[0][0] < gap: # update gap
                minval, _ = h[0]
                maxval, _ = h[-1]
                gap = maxval - minval

        return [minval, maxval]



# heap solution: same idea,but faster; pop min and record max along the way
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h, maxnum = [], 0
        for i, num in enumerate(nums):
            h.append((num[0], i, 0))
            maxnum = max(maxnum, num[0])
        heapq.heapify(h)
       
        interval = [h[0][0], maxnum]
        while len(h) == len(nums):
            _, i, j = heapq.heappop(h) # pop out the smallest
            if j < len(nums[i]) - 1:
                maxnum = max(maxnum, nums[i][j+1])
                heapq.heappush(h, (nums[i][j+1], i, j+1))
                if maxnum - h[0][0] < interval[1] - interval[0]:
                    interval = [h[0][0], maxnum]
        return interval
         