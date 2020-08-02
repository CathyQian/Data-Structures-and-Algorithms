"""
Maximum Subarray

"""
#Method1: DP similar to Knapsack (take the subarray if its sum > 0)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

# Method2: current sum, keep tracking of minimum current sum and maximum subarray sum. 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
            curr_sum, max_sum, min_sum = 0, -sys.maxsize, 0
            for num in nums:
                curr_sum += num
                max_sum = max(max_sum, curr_sum-min_sum)
                min_sum = min(min_sum, curr_sum)
            return max_sum
# Method 3: divide and conquer, T(n) = 2*T(n/2) + O(n), similar to merge sort, time complexity is O(nlogn)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return None
        l = len(nums)
        if l == 1:
            return nums[0]
    
        # divide and conquer
        lmax= self.maxSubArray(nums[:l//2])
        rmax = self.maxSubArray(nums[l//2:])
    
        cursum = nums[l//2] + nums[l//2-1]
        cmax = cursum
        for i in range(l//2+1, len(nums)):
            cursum += nums[i]
            cmax = max(cmax, cursum)
        cursum = cmax
        for i in range(l//2-1)[::-1]:
            cursum += nums[i]
            cmax = max(cmax, cursum)
        return max(lmax, rmax, cmax)