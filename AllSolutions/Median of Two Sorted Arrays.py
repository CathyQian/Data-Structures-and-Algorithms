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
        
# method2 Binary Search  --- easier
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        
        if m < n:
            n, nums1, m, nums2 = m, nums2, n, nums1
        
        start, end = 0, n # end != n-1
        
        while start <= end:
            pa = start + (end-start)//2
            pb = (n+m+1)//2 - pa
            max_a = -sys.maxsize if pa == 0 else nums1[pa-1]
            min_a = sys.maxsize if pa == n else nums1[pa]
            max_b = -sys.maxsize if pb == 0 else nums2[pb-1]
            min_b = sys.maxsize if pb == m else nums2[pb]
            if max_a <= min_b and max_b <= min_a:
                if (n+m)%2==1:
                    return max(max_a, max_b)  
                else:
                    return (max(max_a, max_b) + min(min_a, min_b))/2
            elif max_a > min_b:
                end = pa - 1
            elif max_b > min_a:
                start = pa + 1  
