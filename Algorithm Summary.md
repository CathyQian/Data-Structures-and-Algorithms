Cheatsheet of time complexity for different algorithms: https://www.bigocheatsheet.com/

## bfs
bfs and dfs are top solutions for finding all path/permutations/combinations. Besides, bfs is also a good option to find shortest path (i.e., string addition/removal/mutation, graph distance) by building the tree layer by layer -- if visited elements won't appear in the tree again, the first time the target is achieved is always the shortest path. dfs can also be used to find count (similar to dynamic programming). 

We need a list to store elements in bfs. Alternatively, we can use two list to store the previous and the current layer and update them along the way. This strategy is especially useful if we want to get results from a specific layer (i.e., min path).

- [Perfect Squares](AllSolutions/Perfect%20Squares.py) (BFS for shortest path)
- [Word Search](AllSolutions/Word%20Search.py)
- [Word Search II](AllSolutions/Word%20Search%20II.py)
- **[Remove Invalid Parenthesis](AllSolutions/Remove%20Invalid%20Parenthesis.py)

## dfs or recursion + backtracking
During dfs, you may change some elements which needs to be recovered after each dfs loop. Make sure to recover them after each dfs loop.
- figure out changing parameters and constants in dfs loops
- figure out returning parameter
- figure out edge cases and stopping criteria
```Python
# dfs template for combination
def dfs(self, arr, start, path, res):
    if len(path) == len(arr):
        res.append(path)
        return
    for i in range(start, len(arr)):
        self.dfs(arr, start+1, path+arr[i], res)

# dfs for permutation
def dfs(self, arr, path, res):
    if not arr:
        res.append(path)
        return
    for i in range(len(arr)):
        self.dfs(arr[:i] + arr[i+1:], path + arr[i], res)
```

```Python
# dfs + backtracking
def dfs(self, arr, start, path, res):
    if len(path) == len(arr):
        res.append(path)
    for i in range(start, len(arr)):
        temp = arr[i]
        arr[i] = '#' # block this element in this dfs loop
        self.dfs(arr, start+1, path+arr[i], res)
        arr[i] = temp # recover this element for future dfs loop
```
- [Partition to K Equal Sum Subsets](AllSolutions/Partition%20to%20K%20Equal%20Sum%20Subsets.py) (**)
- [Unique Paths III](AllSolutions/Unique%20Paths%20III.py) (**)

## dfs + memo (time and space complexity**)
dfs + memo is used if some operations have to be repeated again and again, thus it's easier to put them in a memo hashmap to allow for later retrieval. It's mostly used in string or array partitioning or matching.

1. [Target Sum](AllSolutions/Target%20Sum.py)
2. [Word break](AllSolutions/Word%20Break.py)
3. [Word break II](AllSolutions/Word%20Break%20II.py)
4. [Can I win](AllSolutions/Can%20I%20Win.py)
5. [Longest increasing path in a matrix](AllSolutions/Longest%20Increasing%20Path%20in%20a%20Matrix.py)
6. [Combination Sum IV](AllSolutions/Combination%20Sum%20IV.py)
7. [Palindrome Partitioning](AllSolutions/Palindrome%20Partitioning.py)
8. [Palindrome Partitioning II](AllSolutions/Palindrome%20Partitioning%20II.py)
9. **[k sum (lintcode)](AllSolutions/k%20sum.py)

Summary:
- most commonly seen in array or string slicing to meet certain requirement (targeted total/value, palindrome, something is possible or not). The first intuition is to use dfs, where by moving the starting index of the array or string the problem is essentially the same. 
- start from brutal force, see which part involves duplicated calculation, then try to use memo to record duplicated steps to avoid duplicated calculation
- key needs to be unique enough to represent the duplicated steps, can be the index of the string/matrix, or the path representation (scanned elements), or tuple with multiple elements (a, b, c).

## permutation and combination
- Common way to do permutation using dfs:

```Python
def permute(self, path: str, s: list, result: list):
    if not s:
        result.add(path)
    else:
        for idx in range(len(s)):
            self.dfs(path+s[idx], s[:idx]+s[idx+1:], result)
```

Easy to create too many duplicates if the original string or array has too many duplicated elements.

To avoid this, use the following method to get all permutations:

```Python

def permute(self, path: str, s: list, result: list):
    # assuming s is sorted
    if not s:
        result.add(path)
    else:
        for idx in range(len(s)):
            if idx == 0 or s[idx] != s[idx-1]:
                self.dfs(path+s[idx], s[:idx]+s[idx+1:], result)
                    
```

- Python also has its own permutation and combination function
```Python
import itertools
itertools.permutations(iterative)
itertools.combinations(iterative, r) # return r length subsequences of elements from the input iterable
itertools.product(*iterables, repeat=1) # Cartesian product of input iterables. Roughly equivalent to nested for-loops in a generator expression. For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
itertools.product([a,b,c,d], repeat=3) # (x, y, z) for x in [a,b,c,d] for y in [a,b,c,d] for z in [a,b,c,d] 
```

```Python
# 24 game
class Solution:
    def judgePoint24(self, nums):
        if len(nums) == 1:
            return math.isclose(nums[0], 24) # cannot use == as / in python will keep limited decimal points (depending on # of bits used to represent each number)
        for a, b, *rest in itertools.permutations(nums):
            # rest is a list here
            for x in {a+b, a-b, a*b, b and a/b}:
                if self.judgePoint24([x] + rest):
                    return True
        return False
```

- template for using dfs for combination
```Python
# combination sum, no duplicates in candidates, each elements can be used multiple times
class Solution(object):
    def combinationSum(self, candidates: list, target: int) -> list:
        result = []
        self.dfs(sorted(candidates), result, 0, [], target)
        return result

    def dfs(self, candidates, result, start, path, target): # remember these five params
        if target == 0 and path:
            result.append(path)
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > target: # require sort first to allow early termination
                    break
                else:
                    self.dfs(candidates, result, i, path + [candidates[i]], target - candidates[i])
                    # if each elements can only be used once
                    #  self.dfs(candidates, result, i+1, path + [candidates[i]], target - candidates[i])

# combination sum ii, may have duplicates, each number used once
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()                      
        result = []
        self.dfs(candidates, 0, [], result, target)
        return result

    def dfs(self, nums, start, path, result, target):
        if target == 0:
            result.append(path)
            return

        for i in range(start, len(nums)):
            # there may be duplicates in this array
            if i > start or nums[i] == nums[i - 1]:
                continue

            if nums[i] <= target:
            	# each elements can be used only once
            	self.dfs(nums, i + 1, path + [nums[i]], result, target - nums[i])
        return

# combination sum iii, fixed number of elements = k, no duplicates, each number used once
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(n, k, 1, [], res)
        return res

    def dfs(self, target, k, start, path, res):
        if k == 0 and target == 0:
            res.append(path)
           return 

        for i in range(start, 10):
            if target >= i: # make the code faster
                self.dfs(target-i, k-1, i+1, path + [i], res)
        return

# Combination Sum IV, permutations instead of combinations, no duplicates, each number can be used multiple times, return number of permutations ---> dp or dfs
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort() # needed to terminate for loop earlier
        self.memo = {} # target: count hashmap
        return self.dfs(nums, target)
    
    def dfs(self, nums, target):
    	if target not in self.memo:
	    ans = 0
	    for num in nums:
		if target == num:
		    ans = ans+1
		elif target > num:
		    if target-num not in self.memo:
			subans = self.dfs(nums, target-num) # need to introduce index if it's combination instead of permutation
			self.memo[target-num] = subans
		    ans += self.memo[target-num]
	    self.memo[target] = ans
        return self.memo[target]
```

```Python
# factor combinations
class Solution:
    def getFactors(self, n):        
        result = []         
        self.getResult(n, result, [])        
        return result    

    def getResult(self, n, result, factors):        
        i = 2 if not factors else factors[-1] # returning elements in increasing order, to avoid duplicates (combinations instead of permutations)   
        while i <= n // i:            
            if n % i == 0:                      
                result.append(factors + [i, n//i])
                self.getResult(n // i, result, factors + [i])        
            i += 1
```

- template for using dfs for permutation

```Python
# permutations, nums don't contain duplicates
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, path):
        if len(nums) == 0 and path:
            res.append(path)
        # main difference between permutation and combination:
        # combination: for i in range(start, len(nums)) --> dfs(nums, i+1, path, res)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], res, path + [nums[i]])
            # self.dfs(nums, res, path + nums[i]) # if nums can be used many times

# permutations II, nums contains duplicates
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(sorted(nums), res, [])
        return res
    
    def dfs(self, nums, res, path):
        if len(nums) == 0 and path:
            res.append(path)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]: # same logic as before, to avoid duplicates
                self.dfs(nums[:i] + nums[i+1:], res, path + [nums[i]])

# similar problem: palindrome permutation II
```

- [Palindrome Permutation II](AllSolutions/Palindrome%20Permutation%20II.py) (tricky permutaion to avoid duplicates)

## string operations
Common problems include searching for the longest substring/subsequence/palindrome substring/palindrome subsequence. Note substring needs to be consecutive while subsequence not. Common methods involves dp, dfs, bfs(shortest path) and basic string operations. Search can start from the beginning, move towards right, or vice versa; or start from both ends, move towards the middle, or vice versa (- [Longest Palindromic Substring](AllSolutions/Longest%20Palindromic%20Substring.py)).

Common knowledge:
```Python
ord('A') == 65
chr(65) == 'A'
ord('a') == 97
s = s.lower() # lowercase all characters in s
s = s.upper() # uppercase all characters in s
sorted(list(collections.Counter(newlist).items()), key=lambda x: x[1])[-1][0]
paragraph = re.sub('[!@#$?:;\'\".,]', ' ', paragraph) # regular expression, equivalent to code below
for c in "!?',;.":
	paragraph = paragraph.lower().replace(c, " ")

s1[:i] (i elements) and s2[:j] (j elements) -> s3[:i+j] (i+j elements)
shortest = min(strs, key=len) # find shortest string
```

Some code snippets as template.
```Python
class Solution:
    def longestCommonSubstring(self, s1, s2):
        if not s1 or not s2:
            return 0
        m, n = len(s1), len(s2)
        ans = 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    ans = max(ans, dp[i+1][j+1])
                else: # major difference from subsequence
                    dp[i+1][j+1] = 0
        return ans

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[m][n]
```

```Python
# figure out value of a number in string format, iterative solution template
def value(s: str) -> int:
    res = 0
    for ss in s:
        if ss.isdigit():
            res = res*10 + int(ss)
        else:
            break
    return res
```

```Python
# random generator (code snippets from Markov Chain)
    def randomWord(self, wordict):     
        total = 0     
        for key, value in wordict.items():         
            total += value 

        randindex = random.randint(1, total) # [1, total]
        for key, value in wordict.items():  # output is random       
            randindex -= value         
            if randindex <= 0:             
                return key 
```

```Python
# dp template: the hardest part is to figure out which direction each index scan. This can be figured out by using the dp relationship.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n)[::-1]: # or i from 1 to n, j from i-1 to 0
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

"""   
Idea:
- This problem is quite similar to find longest Palindromic substring (iterate through each element, 
for each element, search both left and right for the same element). The difference here is that it's 
looking for subsequence which the elements doesn't need to be adjacent to each other.

- For such types of questions where min/max number of combinations is needed, dynamic programming is a top choice.
- For dp,let's define
 - state: dp[i][j] represents the longest palindromic subsequence between s[i] and s[j], including s[i] and s[j]
 - function:
 if s[i] = s[j], dp[i][j] = dp[i+1][j-1]+2
 if s[i] != s[j], dp[i][j] = max(dp[i+1][j], dp[i][j-1]) (this relationship is where I find difficult. For substring, 
 since all elements needs to be adjacent, this relationship is not true anymore)

```
```Python
# The other one is KMP algorithm (https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/)
# Longest Happy Prefix

class Solution:
    def longestPrefix(self, t: str) -> str:
        i, j, lps = 1, 0, [0]*len(t)
        while i < len(t):
            if t[i] == t[j]:
                j, lps[i] = j + 1, j + 1
                i += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        return t[:lps[-1]]
```
## Dynamic Programming
Dynamic programming is usually used to find max/min, yes/no, count. Sometimes can be used interchangably with dfs.
Other cases to use dynamic programming involves problems has overlapping subproblems property (all DP, similar as recursion) or multi-variable where a dp matrix can be constructed. Once, we observe these properties in a given problem, be sure that it can be solved using DP.

Four components of dp solution:
- state (matrix DP, sequence, two sequences DP, backpack)
- function
- initialization (where's the starting point?)
- result (where's the ending point?)

Sometimes it's hard to think of dp solution directly. A common strategy is to start with brutal force and then think about how to reduce redundant steps. A good reference can be found here: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/solution/
**Alternatively, try to convert the problem into a 2D (or 3D matrix) problem, fill in status gradually.**
- Classical problem 1: backpack problem. Use 2D dp matrix can easily solve the problem given two parameters. Alternatively, 2D dp matrix can be replaced by two 1D array pre and post which are updated interwavingly. 

```Python
# backpack I
"""
Given n items with size A[i], an integer m denotes the size of a backpack. How full you can fill this backpack?
"""
"""
This is a classical problem to use dynamic programming.
state f[j]: maximum sum item size when backpack size is j and A[0:i+1] elements are allowed to put into 
            the backpack.
function: if j >= A[i]: f[j] = max(pre[j], pre[j - A[i]] + A[i])
          else: f[j] = pre[j]
initialization:f = [0 for _ in range(m)]
return f[m-1]

"""
# Space O(m*n) or O(m)
class Solution:
    def backPack(self, m, A):
        pre = [0 for _ in range(m+1)] # 2D or 1D, n increment gradually
        n = len(A)
        for i in range(n):
            post = pre.copy() # important, pre and post are pointing to the same object, any changes in post will also modify the corresponding elements in pre
            for j in range(1, m+1):
                if j >= A[i]:
                    post[j] = max(pre[j], pre[j-A[i]] + A[i])
            pre = post
        return pre[-1]

# backpack II
"""
Given n items with size A[i] and value V[i], and a backpack with size m. 
What's the maximum value can you put into the backpack?
"""
# similar to backPackI but replace A with V when calculating f
class Solution:
    def backPackII(self, m, A, V):
        pre = [0 for _ in range(m+1)]
        for i in range(len(A)):
            post = pre.copy() # shallow copy
            for j in range(1, m+1):
                if j >= A[i]:
                    post[j] = max(pre[j], pre[j-A[i]] + V[i])
            pre = post
        return pre[-1]

# minimum adjustment cost (2 parameters, hidden backpack problem) (similar problems: paint house)
class Solution:
    def MinAdjustmentCost(self, A, target):
        maxNum = 100
        pre_dp = [0]*(maxNum+1)
        
        for i in range(len(A)):
            post_dp = [None]*(maxNum+1)
            for cur in range(0, maxNum+1):
                post_dp[cur] = min([pre_dp[pre] + abs(cur -A[i]) for pre in range(0, maxNum+1) if abs(pre-cur) <= target])
            pre_dp = post_dp
            
        return min(post_dp)

```

- Classical problem 2: triangle problem (half matrix, there is directionality). It provides a common template for min/max path problem.
```Python
# top down vs bottom up (easier because of less path), very common for matrix (2D array) operation

class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = triangle[-1]
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]

        return dp[0]
```

- classical problem 3: paint house (similar to triangle problem, full matrix, so no directionality)
```Python
# top down method 
# use two list, update values with every new house
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        pre = [0, 0, 0]
        for cost in costs:
            cur = [0]*3 # need to reset cur at the beginning of each loop
            cur[0] = cost[0] + min(pre[1], pre[2])
            cur[1] = cost[1] + min(pre[0], pre[2])
            cur[2] = cost[2] + min(pre[0], pre[1])
            pre = cur
        return min(pre)

# also top down method, use one list, update values with every new house
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        row = [0, 0, 0]
        for r in costs:
            row[0], row[1], row[2] = r[0] + min(row[1], row[2]), r[1] + min(row[0], row[2]), r[2] + min(row[0], row[1])
        return min(row)
```

- classical problem 4: edit distance (shortest path from one string to another)
```Python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        f = [[0 for j in range(n+1)] for i in range(m+1)] # make sure to add additional dimensions to the dp matrix to allow for cold start
        for i in range(m+1):
            f[i][0] = i
        for j in range(n+1):
            f[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min(f[i-1][j]+1, f[i][j-1]+1, f[i-1][j-1]+1) # three different editing methods
        return f[m][n]
```

## binary search (array and matrix)
- array is relatively easy while rotated array is a little tricky; things get more complicated if there is duplicates in the array
Common steps involved are 
- 1) find the mid element 
- 2) tell if mid is in the same branch as start or end using if/else 
- 3) tell target is between start and mid or between mid and end, take next step. If duplicates is found, move start one step forward, update mid again.

```Python
# Find Minimum in Rotated Sorted Array I
# no duplicates in the array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        start, end = 0, len(nums) - 1
        while start+1 < end: # two elements left when out of while loop
            mid = start + (end - start)//2
            # notice there are only three conditions: (1) start & mid & end in one branch; (2) start & mid in one branch, end in the other; (3) mid & end in one branch, start in the other
            if nums[mid] > nums[start] and nums[mid] < nums[end]: # (1), min element found
                return nums[start]
            elif nums[mid] > nums[start] and nums[start] > nums[end]: # (2)
                start = mid # not start = mid + 1, no skipping elements
            else: # (3)
                end = mid # not end = mid - 1, no skipping elements
        return min(nums[start], nums[end])

# Find Minimum in Rotated Sorted Array II
# There is duplicates in the array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        start, end = 0, len(nums) - 1
        while start+1 < end: 
            mid = start + (end - start)//2
            if nums[mid] == nums[start]: # add when duplicates allowed
                start += 1
            elif nums[mid] > nums[start] and nums[mid] <= nums[end]:
                return nums[start]
            elif nums[mid] > nums[start] and nums[start] >= nums[end]:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])
```

```Python
# Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]: # tell if mid and start are in the same branch, only one senario
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else: # nums[mid] < nums[start]:
                if target <= nums[end] and nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1



```
- matrix has some tricks
There are a couple of types of matrix and different binary search methods are used:

```Python
# type 1: can be stretched to an ordered 1D array directly (each row is sorted in ascending order, first element of the next row is larger than last element of the previous row) Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r-l)//2
            row, col = mid // n , mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
```

```Python
# Type 2: can not be stretched to an ordered 1D array directly (each row is sorted in ascending order, first element of the next row is not necessarily larger than last element of the previous row), Search a 2D Matrix II
# Solution 1: efficient search, this is different from binary search though. O(m + n)
# This is a classical way to search in partially ordered matrix. You can start
# from matrix[m-1][n-1] or matrix[m-1][0] or matrix[0][n-1] or matrix[0][0]. 
# Be adaptive to the problem. Don't always stick to binary search. Indeed, binary
# search won't work well here since it will over-filter elements.
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        row, col = len(matrix), len(matrix[0])
        cr, cc = 0, col - 1
        while cr < row and cc >= 0:
            if matrix[cr][cc] == target:
                return True
            elif matrix[cr][cc] > target:
                cc -= 1
            else:
                cr += 1

        return False
        
# Solution 2: divide and conquer, O(nlogn) time
# This is a smart binary search. Very easy to make mistakes though.
# ref:https://www.geeksforgeeks.org/search-in-a-row-wise-and-column-wise-sorted-2d-array-using-divide-and-conquer-algorithm/
# It's easy to make mistakes on index using this method
```
- binary search for intervals operation, be careful with the index
```Python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: 
        bounds = []
        for i in range(len(newInterval)):
            left, right = 0, len(intervals)-1
            while left <= right:
                mid = left+(right-left)//2
                if intervals[mid][0] <= newInterval[i]: # find left and right bound for newInterval
                    left = mid + 1
                else:
                    right = mid - 1
            bounds.append([left, right])
            
        left_bound, right_bound = bounds[0][1], bounds[1][0]
        
        result = intervals[:left_bound+1]
        if not result or result[-1][1]<newInterval[0]:
            result.append(newInterval)
        else:
            result[-1][1]= max(result[-1][1], newInterval[1])
            
        for idx in range(left_bound+1, right_bound):
                result[-1][1]= max(result[-1][1], intervals[idx][1])
        return result + intervals[right_bound:]
```

## Linked list 
Not hard, but need some templates to make coding faster

Find mid point of a linked list using slow and fast pointer

```Python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# It's very likely that the head of the linked list will be modified or even deleted, so add a Dummy node and define Dummy.next = head, then return Dummy.next

```

1. Reverse a linked list

```Python
def reverse(self, head):
    if not head or not head.next:
        return head
    pre, cur = None, head
    while cur:
        post = cur.next
        cur.next = pre
        pre, cur = cur, post
    return pre
```

2. Detect cycle

```Python
# test if there is cycle or not
def hasCycle(self, head: ListNode) -> bool:
    if not head or not head.next:
        return False
    slow, fast = head, head
    while fast and fast.next: # can't be just fast.next
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# return position of the cycle

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
            
        return None
```

3. Copy list with random pointer
```Python
import collections
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = collections.defaultdict(lambda: Node(0)) # need lambda function here since default data type is only list or int or set
        dic[None] = None
        cur = head
        while cur:
            dic[cur].val = cur.val
            dic[cur].next = dic[cur.next]
            dic[cur].random = dic[cur.random]
            cur = cur.next
        return dic[head]

```
4. Insert/remove elements in linked list (refer to notebook)

5. minheap
```Python
# implement a min heap
# also need to remember heapsort, keep pop out the min element
class MinHeap: 

    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0 # # of elements in heap, decide on the end of the heap (notice the extra numbers are not removed)
        self.Heap = [0]*(self.maxsize) # index starts from 0

    def heapifyHelper(self, pos):
        # percolation down (from top to bottom), O(logn)
        if 2*pos + 1 < self.size: # if it is not a leave (has at least one child)
            smallest = pos
            l_pos, r_pos = 2 * pos + 1, 2 * pos + 2
            if l_pos < self.size and self.Heap[l_pos] < self.Heap[smallest] :
                smallest = l_pos
            if r_pos < self.size and self.Heap[r_pos] < self.Heap[smallest]:
                smallest = r_pos
            if smallest != pos:
                self.Heap[smallest], self.Heap[pos] = self.Heap[smallest], self.Heap[pos]
                    self.heapifyHeaper(smallest) 

    def heapify(self):
        # transform an unsorted list to a minheap, O(n) --- why is it O(n)? worst case scenario
        for pos in range((self.size - 1) // 2, -1, -1): # don't consider leaves
            self.heapifyHelper(pos) 
            
    # Function to insert a node into the heap 
    def push(self, element):
        # percolation up (bottom to up), O(logn)
        if self.size >= self.maxsize: 
            return
        self.Heap[self.size] = element # add as leave
        
        curr = self.size 
        parent = (curr - 1) // 2
        while self.Heap[curr] < self.Heap[(parent)]: # swap with parent
            self.Heap[curr], self.Heap[parent] = self.Heap[parent], self.Heap[curr] 
            curr = parent
            parent = (curr-1)//2
        
        self.size += 1

    def pop(self): # O(logn)
        popped = self.Heap[0] # O(1)
        self.Heap[0] = self.Heap[self.size-1] 
        self.size -= 1
        self.heapifyHelper(0)
        return popped 
    
    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(self.size//2): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+
                                str(self.Heap[2 * i + 1])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 2])) # may have no right child

# Driver Code 
# note the heap can be initialized either by push or heapify (two different routes)
if __name__ == "__main__": 
    print('The minHeap is ') 
    minHeap = MinHeap(15) 
    minHeap.push(5) 
    minHeap.push(3) 
    minHeap.push(17) 
    minHeap.push(10) 
    minHeap.push(84) 
    minHeap.push(19) 
    minHeap.push(6) 
    minHeap.push(22) 
    minHeap.push(9) 
    minHeap.minHeap() 

    minHeap.Print() 
    print("The Min val is " + str(minHeap.pop())) 
    minHeap.Print()
```
6. trie
```Python
# implement a trie
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.vals = set() # can easily remove and do a regular search

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[word] = word 
        self.vals.add(word)
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.vals:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            else:
                node = node[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
"""

```


# create new data structure if too many parameters to hold

Example, LFU Cache
```Python
# both LFU and LRU mentioned recency, so what data structure can record recency --- deque and OrderedDict
# difference: LFU also needs to record count, so hashmap to record key-value pair is not enough
# needs key-value-count instead, create a node class to make things easier, then use hashmap key-node to allow easy
# access of keys, use count: {key: node} to find node with minimum count

# LFUCache: quite hard
from collections import defaultdict
from collections import OrderedDict

class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.space = capacity
        self.key2node = {} # key:node(key, val, count)
        self.count2node = defaultdict(OrderedDict) # {count: {key: node}}
        self.minCount = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1

        node = self.key2node[key]
        del self.count2node[node.count][key]
        # clean memory
        if not self.count2node[node.count]: # if empty, clean memory
            del self.count2node[node.count]
        node.count += 1
        self.count2node[node.count][key] = node
        # NOTICE check minCount!!! the deleted count in count2node was mincount
        if not self.count2node[self.minCount]:
            self.minCount += 1
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """  

        if self.space == 0 and not self.key2node:
            return

        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key) # NOTICE, put makes count+1 too
        else: 
            if self.space == 0: # cache is not empty
                # popitem(last=False) is FIFO, like queue
                # it return key and value!!!
                k, n = self.count2node[self.minCount].popitem(last=False) # the most important line of code
                del self.key2node[k] 
                self.space += 1
            self.key2node[key] = Node(key, value, 1)
            self.count2node[1][key] = self.key2node[key] 
            self.minCount = 1
            self.space -= 1

        return
```

# sliding window problem

[Sliding Window Medium](AllSolutions/Sliding%20Window%20Median.py)
```Python
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
```

[Sliding Window Maximum](AllSolutions/Sliding%20Window%20Maximum.py)
```Python
# only  store elements bigger than the last element stored in the window
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: 
        res = []
        q = deque()
        for i in range(len(nums)):
            if q and q[0] == i - k:
                _ = q.popleft()
            while q and nums[q[-1]] < nums[i]:
                _ = q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
```

# union find
Find cluster/subsets in graphs
every subset only have one parent if nodes parents fully updated (use find function before parent in case**)

# jump game
try dfs or bfs or heuristic method, try to avoid dp
