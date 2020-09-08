## bfs
bfs and dfs are top solutions for finding all path/permutations/combinations. Besides, bfs is also a good option to find shortest path by building the tree layer by layer. If visited elements won't appear in the tree again, the first time the target is achieved is always the shortest path.

- [Perfect Squares](AllSolutions/Perfect%20Squares.py) (BFS for shortest path)
- [Word Search](AllSolutions/Word%20Search.py)
- [Word Search II](AllSolutions/Word%20Search%20II.py)
- **[Remove Invalid Parenthesis](AllSolutions/Remove%20Invalid%20Parenthesis.py)

## dfs + backtracking
During dfs, you may change some elements which needs to be recovered after each dfs loop. Make sure to recover them after each dfs loop.

```Python
# Common dfs
def dfs(self, arr, start, path, res):
    if len(path) == len(arr):
        res.append(path)
    for i in range(start, len(arr)):
        self.dfs(arr, start+1, path+arr[i], res)
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
dfs + memo is used if some operations have to be repeated again and again, thus it's easier to put them in a memo hashmap to allow for later retrieval.

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
            if s[start] != s[i] or start == i:
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