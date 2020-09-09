一是只要遇到字符串的子序列或配准问题首先考虑动态规划DP (shortest path --- bfs or dp)，二是只要遇到需要求出所有可能情况首先考虑用递归dfs (for combination or for permutation)

## bfs
bfs and dfs are top solutions for finding all path/permutations/combinations. Besides, bfs is also a good option to find shortest path by building the tree layer by layer. If visited elements won't appear in the tree again, the first time the target is achieved is always the shortest path.

- [Perfect Squares](AllSolutions/Perfect%20Squares.py) (BFS for shortest path)
- [Word Search](AllSolutions/Word%20Search.py)
- [Word Search II](AllSolutions/Word%20Search%20II.py)
- **[Remove Invalid Parenthesis](AllSolutions/Remove%20Invalid%20Parenthesis.py)

## dfs + backtracking
During dfs, you may change some elements which needs to be recovered after each dfs loop. Make sure to recover them after each dfs loop.

```Python
# dfs template for combination
def dfs(self, arr, start, path, res):
    if len(path) == len(arr):
        res.append(path)
    for i in range(start, len(arr)):
        self.dfs(arr, start+1, path+arr[i], res)

# dfs for permutation
def dfs(self, arr, path, res):
    if not arr:
        res.append(path)
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
- [Partition to K Equal Sum Subsets](AllSolutions/Partition%20to%20K%20Equal%20Sum%20Subsets.py)
- [Unique Paths III](AllSolutions/Unique%20Paths%20III.py)

## dfs + memo
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
def permute(self, s: str, start: int, result: list):
    if start == len(s):
        result.add(''.join(s))
    else:
        for i in range(start, len(s)):
            if s[start] != s[i] or start == i: # s is sorted first, avoid duplicates
                s[start], s[i] = s[i], s[start] 
                self.permute(s, m, start+1) 
                # make sure to recover the array for the next iteration
                s[start], s[i] = s[i], s[start]
                    
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

    def dfs(self, candidates, result, start, path, target):
        if target == 0 and path:
            result.append(path)
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > target: # require sort first to allow early termination
                    break
                else:
                    self.dfs(candidates, result, i, path + [candidates[i]], target - candidates[i])
                    # if each elements can only be used once
                    # self.dfs(candidates, result, i+1, path + [candidates[i]], target - candidates[i])

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
            if i > start and nums[i] == nums[i - 1]:
                continue

            if nums[i] > target:
                break
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
        ans = 0
        for num in nums:
            if target == num:
                ans = ans+1
            elif target > num:
                if target-num not in self.memo:
                    subans = self.dfs(nums, target-num)
                    self.memo[target-num] = subans
                ans += self.memo[target-num]
            else:# target < num
                self.memo[target] = ans
                return ans
        self.memo[target] = ans
        return ans
```

```Python
# factor combinations
class Solution:
    def getFactors(self, n):        
        result = []         
        self.getResult(n, result, [])        
        return result    

    def getResult(self, n, result, factors):        
        i = 2 if not factors else factors[-1] # returning elements in increasing order      
        while i <= n / i:            
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


## others
- matrix operation, the first thing is to check for empty matrix
```Python
if not mtx or not mtx[0]:
    return None
```
- array operation, sort and skip elements if it is the same as the one before it to avoid duplicates in permutation and combination

## string operations
Common problems include searching for the longest substring/subsequence/palindrome substring/palindrome subsequence. Note substring needs to be consecutive while subsequence not. Common methods involves dp, dfs and basic string operations. Search can start from the beginning, move towards right, or vice versa; or start from both ends, move towards the middle, or vice versa (- [Longest Palindromic Substring](AllSolutions/Longest%20Palindromic%20Substring.py)).

Common knowledge:
```Python
ord('A') == 65
chr(65) == 'A'
ord('a') == 97

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
        for i in range(n)[::-1]:
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

"""   
Idea:
- This problem is quite similar to find longest Palindromic subsequence (iterate through each element, 
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
        pre = [0 for _ in range(m+1)]
        n = len(A)
        for i in range(n):
            post = pre.copy() # important
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

# minimum adjustment cost (2 parameters, hidden backpack problem)
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
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
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
- array is relatively easy
- matrix has some tricks

```

```
## array and matrix
- quick sort: note only put elements bigger or smaller in front of the pivot, if there is elements equal to pivot, put it behind the pivot (see notes below).
```Python
# Kth Largest Element in an Array
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
            print(nums[j], pivot)
            if nums[j] > pivot:# there is duplicated elements, ignore equal elements
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j +=1
        nums[left], nums[i-1] = nums[i-1], nums[left]
        return i-1
```
- binary search to find target elements/order in sorted array or matrix