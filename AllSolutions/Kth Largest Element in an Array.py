"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted 
order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

"""
"""
Similar problem:kth smallest element in an unsorted array
"""

# Solution 1: sort and then output, O(nlogn) time, O(1) space
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort(reverse = True)
        return nums[k-1]

# Solution 2: use minHeap to keep the k largest elements
# Time complexity: O(Nlogk)
# Space complexity: O(k) to store the heap elements 
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

# Solution 3: quick select (similar to quicksort)
# Time complexity: O(N) in the average case, O(N2) in the worst case.
# Space complexity: O(1).

class Solution:
    def findKthLargest(self, nums, k):
        left, right = 0, len(nums)-1
        while left <= right:    
            pos = self.partition(nums, left, right)
            print(pos, nums)
            if pos == k-1:
                return nums[pos]
            elif pos > k-1:
                right = pos -1
            else:
                left = pos + 1
    
    def partition(self, nums, left, right):
        # similar to quick sort
        pivot = nums[left]
        i, j = left+1, left + 1
        while j < len(nums):
            if nums[j] > pivot:# there is duplicated elements, ignore equal elements, think about [5,5,6] you want to get [6,5,5]
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j +=1
        nums[left], nums[i-1] = nums[i-1], nums[left]
        return i-1
        
