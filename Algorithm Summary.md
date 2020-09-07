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
Common way to do permutation using dfs:

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

- [Palindrome Permutation II](AllSolutions/Palindrome%20Permutation%20II.py) (tricky permutaion to avoid duplicates)


## others
matrix operation, the first thing is to check for empty matrix
```Python
if not mtx or not mtx[0]:
    return None
```