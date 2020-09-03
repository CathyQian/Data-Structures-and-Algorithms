"""
Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return None
        m, n = len(nums1), len(nums2)
        if (m+n+1)%2 == 0:
            return self.findKth(nums1, nums2, 0, 0, (m+n+1)//2)
        else:
            l = self.findKth(nums1, nums2, 0, 0, (m+n+1)//2)
            r = self.findKth(nums1, nums2, 0, 0, (m+n+2)//2)
            return (l+r)/2
        
    def findKth(self, A, B, A_start, B_start, k):
        if A_start >= len(A):
            return B[B_start+k-1]
        if B_start >= len(B):
            return A[A_start+k-1]
        
        if k == 1:
            return min(A[A_start], B[B_start])
        
        A_key = A_start + k//2 - 1
        B_key = B_start + k//2 - 1
        
        if A_key < len(A) and B_key < len(B) and A[A_key] < B[B_key] or B_key >= len(B):
            return self.findKth(A, B, A_start + k//2, B_start, k - k//2)
        else:
            return self.findKth(A, B, A_start, B_start + k//2, k - k//2)