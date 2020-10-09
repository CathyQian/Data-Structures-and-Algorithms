## array
- quick sort: note only put elements bigger or smaller in front of the pivot, if there is elements equal to pivot, put it behind the pivot (see notes below).
The major difference between quick sort and merge sort is that for quick sort, you can quickly find the position of the kth elements without ordering the elements bigger or smaller than it. So it is a good choice to find the kth largest/smallest elements in an array.
Quick sort: time complexity -- worst O(n2), best/average O(nlogn)
```Python
# Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums, k):
        left, right = 0, len(nums)-1
        while left <= right: # similar logic as binary search
            pos = self.partition(nums, left, right) # after partition, nums[:pos] and nums[pos+1:] are already sorted
            if pos == k-1:
                return nums[pos]
            elif pos > k-1:
                right = pos -1 # sort nums[:pos]
            else:
                left = pos + 1 # sort nums[pos+1:]
    
    def partition(self, nums, left, right): # use the whole nums so that returning index is relative to the whole string
        # quick sort
        pivot = nums[left]
        i, j = left+1, left + 1 # pay attention to the index
        while j < len(nums):
            if nums[j] > pivot:# if there is duplicated elements, ignore equal elements; otherwise, some later bigger elements won't be able to swap, think about [5,5,6]
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j +=1
        nums[left], nums[i-1] = nums[i-1], nums[left] # pay attention to the index
        return i-1
```
- binary search to find target elements/order in sorted or rotated array or matrix (see binary search section)

- sum combinations, usually do a one-pass scan and use hashmap to record cursum or cursum frequency

Example 1: Subarray Sum Equals K (hashmap to store residual)
```Python
# Subarray Sum Equals K
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, cumsum = 0, 0
        lookup = collections.defaultdict(int) # default value all 0
        lookup[0] = 1
        for num in nums:
            cumsum += num
            res += lookup[cumsum-k]
            lookup[cumsum] += 1
        return res
```

- Multiple pointers
    - Two pointers: one to scan the current element, the other one to record min/max along the way
    - Three pointers: one scan from the beginning, one scan from the end, another one start from the beginning to allow swapping or record elements (i.e., Merge Sorted Array, Sort Colors)
Example 1: # Sort Colors
```Python
# one-pass solution, pay attention to i change when nums[i] == 0
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, l, r = 0, 0, len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1 # nums[i] == 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
        return 

Example 2: Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if nums[i] != num:
                i += 1
                nums[i] = num
        return i + 1
```

Example 3: insertion sort

```Python
# Sliding Window Median
# time complexity: O((n-k+1)*logn)
class Solution:
    def medianSlidingWindow(self, nums, k):
        if k == 0: return []
        ans = []
        window = sorted(nums[0:k]) # maintain a sorted window
        for i in range(k, len(nums)):
            ans.append((window[k // 2] + window[(k - 1) // 2]) / 2.0) # concise!
            index = bisect.bisect_left(window, nums[i - k]) # log(n)
            window.pop(index)      
            bisect.insort_left(window, nums[i]) # log(n)
        return ans
```

Example 4: search for pairs in array
```Python
# K-diff Pairs in an Array (unique pair)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        visited = set()
        count = 0
        for num in nums:
            if num not in visited:
                if k == 0 and nums.count(num) > 1:
                    count += 1 # if not unique pair, count += nums.count(num)//2
                    visited.add(num)
                elif k != 0 and num+k in nums:
                    count += 1
                    visited.add(num)
        return count

```
Other examples include two sum, 3 sum, 4 sum.

- divide and conquer (very useful for array, split in half, then combine) (a type of recursion)

Example 1: Maximum Subarray
```Python
# Maximum Subarray
#Method1: DP similar to Knapsack (take the subarray if its sum > 0)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1] # only add previous cursum if positive
        return max(nums)

# Method2: current sum, keep tracking of minimum current sum and maximum subarray sum. 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
            curr_sum, max_sum, min_sum = 0, -sys.maxsize, 0
            for num in nums:
                curr_sum += num
                # The following two lines can not be reversed
                max_sum = max(max_sum, curr_sum-min_sum) # maxsum and minsum are different stages of cursum
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
```

Example 2: Different Ways to Add Parentheses
Note: different from **Expression Add Operators** which cannot use parentheses, so the combination is more difficult.

```Python
# Different Ways to Add Parentheses
class Solution(object):
    def diffWaysToCompute(self, input):
        res = [] 
        if input.isdigit():
            return [eval(input)]
        for i, char in enumerate(input):
            if char in "+-*":
                part1 = self.diffWaysToCompute(input[:i])
                part2 = self.diffWaysToCompute(input[i + 1:])
                for x in part1:
                    res += [eval(str(x) + char + str(y)) for y in part2]
       
        return res

# use memo to make solution faster
class Solution(object):
    global memo
    memo = {}
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [eval(input)]
        if input not in memo:
            res = []
            for i, char in enumerate(input):
                if char in "+-*":
                    part1 = self.diffWaysToCompute(input[:i])
                    part2 = self.diffWaysToCompute(input[i + 1:])
                    for x in part1:
                        res += [eval(str(x) + char + str(y)) for y in part2]
            memo[input] = res
        return memo[input]
```

- interval operation (use stack)
```Python
# Merge Intervals
# It's not really a stack, but rather a list.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return None
        intervals.sort()
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], intervals[i][1])
            else:
                stack.append(intervals[i])
        return stack
```

- min steps to reach a point

```Python
# Minimum Number of Taps to Open to Water a Garden
# change into an interval problem, sort first, then iterate one by one to find max end

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        if n < 2:
            return -1
        intervals = []
        for i, r in enumerate(ranges):
            intervals.append((max(0, i-r), min(i+r, n)))
        intervals.sort()
        
        ans, i, l, e = 0, 0, 0, 0
        while e < n: # break when e >= n
            while i <= n and intervals[i][0] <= l: # <=
                e = max(e, intervals[i][1])
                i += 1
            if l == e:
                return -1
            l = e
            ans += 1

        return ans

# similar to jump game II
"""
- The idea is to maintain two pointers left and right, where left initialy set to be 0 and right set to be nums[0].
- So points between 0 and nums[0] are the ones you can reach by using just 1 jump.
- Next, we want to find points I can reach using 2 jumps, so our new left will be set equal to right, and our new right will be set 
equal to the farest point we can reach by two jumps. which is:
right = max(i + nums[i] for i in range(left, right + 1)

"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return 0
        l, r = 0, nums[0]
        steps = 1
        while r < len(nums) - 1:
            steps += 1
            max_r = max([i + nums[i] for i in range(l, r+1)])
            l, r = r, max_r
        return steps
```

## matrix (dealing with index can be tricky)
- spiral matrix
```Python
# Spiral Matrix
# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/178 
# key: update index at every step and stop when index condition violated. If there is any unvisited element, up<=down & left <= right
# if one of such condition is violated, then no unvisited element, stop loop and return

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return None # not return null
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m-1, 0, n-1
        res = []
        while up <= down and left <= right:
            for i in range(left, right+1):
                res.append(matrix[up][i])      
            up += 1
            if up > down: # required
                break
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left: # required
                break
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -= 1
            if up > down: # required
                break
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left += 1
            if right < left: # required
                break
        return res

```

- matrix rotation
```Python
# rotate image
# clockwise rotation = reverse row + matrix transpose
# elements swamp in Python: a, b = b, a

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        # reverse rows
        m, n = len(matrix), len(matrix[0])
        for i in range(m//2):
            matrix[i], matrix[m-1-i] = matrix[m-1-i], matrix[i] 
            
        # matrix transpose
        for i in range(m):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

- binary search in matrix (see binary search section)
