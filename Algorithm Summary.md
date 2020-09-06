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
