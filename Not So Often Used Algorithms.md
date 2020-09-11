1. Morris Traversal of Binary Tree
ref: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/

```Python
# Python program to do Morris inOrder Traversal: 
# inorder traversal without recursion and without stack 
  
class Node: 
    """A binary tree node"""
    def __init__(self, val): 
        self.val = val
        self.left = None 
        self.right = None 
  
def morris_traversal(root): 
    """Generator function for iterative inorder tree traversal"""
    res = []
    curr = root 
    while curr:     
        if not curr.left: 
            res.append(curr.data) 
            curr = curr.right 
        else: 
            pre = curr.left 
            while pre.right and pre.right != curr: 
                pre = pre.right 
  
            if not pre.right:  
                pre.right = curr 
                curr = curr.left         
  
            else: # pre.right == curr
                pre.right = None
                res.append(curr.data) 
                curr = curr.right
    return res
              
```

```Python
# binary tree in-order traversal (iterative solution, another solution is recursive solution)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        cur = root
        res = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

```
2. Next permutation
ref: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

```Python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]: # make sure the direction is correct
            i -= 1
        if i == 0:
            nums.reverse()
            return
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
      
```

3. Moore voting algorithm -- Majority Element I, II
```Python
# Majority Element
"""
Boyer-Moore Majority Voting Algorithm (or Moore Voting)

The idea is that we use two additional variables:

    candidate: to keep track of the potential candidate at each step.
    counter: the number of appearance of the candidate at that step.

Initially, the current candidate is None and the counter is 0. As we iterate the array over an element e, we will do the following check:

    If the counter is 0, we set the current element e as the new candidate.
    If the counter is not 0, we will check:
    If the current element e is the same as the candidate, we increment the counter by 1
    Else we decrement the counter by 1
"""
# both can be replaced by hashmap
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        V = [None, 0]
        for num in nums:
            if V[1] == 0:
                V = [num, 1]
            elif num == V[0]:
                V[1] += 1
            else:
                V[1] -= 1
        return V[0] 

# Majority element II
class Solution(object):
    def majorityElement(self, nums):
        v1 = [None, 0]
        v2 = [None, 0]
        for num in nums:
            if v1[1] == 0:
                v1 = [num, 1]
            elif v2[1] == 0:
                v2 = [num, 1]
            elif num == v1[0]:
                v1[1] += 1
            elif num == v2[0]:
                v2[1] += 1
            else:
                v1[1] -= 1
                v2[1] -= 1
        return [v for v in (v1[0], v2[0]) if nums.count(v) > len(nums)//3]
```
4. KMP algorithm (pattern search) -- longest happy prefix
Time complexity of naive pattern searching algorithm is O(m(n-m+1)). It doesn’t work well in cases where we see many matching characters followed by a mismatching character. The time complexity of KMP algorithm is O(n) in the worst case.

The basic idea behind KMP’s algorithm is: whenever we detect a mismatch (after some matches), we already know some of the characters in the text of the next window. We take advantage of this information to avoid matching the characters that we know will anyway match. 
```Python
# KMP algorithm: https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
class Solution:
    def longestPrefix(self, t: str) -> str:
        i, j, lps = 1, 0, [0]*len(t)
        while i < len(t):
            if t[i] == t[j]:
                j, lps[i] = j + 1, j + 1
                i += 1
            else:
                if j != 0:
                    j = lps[j-1] # instead of starting from 0 (brutal force)
                else:
                    lps[i] = 0
                    i += 1
        return t[:lps[-1]]
```
5. State machine (hard to understand, do not use, can be replaced with dynamic programming)
State machine: https://www.youtube.com/watch?v=vwJT2njv6rM

```Python
# Best Time to Buy and Sell Stock III
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = -sys.maxsize
        sell1 = 0
        buy2 = -sys.maxsize
        sell2 = 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1-price)
            sell2 = max(sell2, buy2 + price)
        return sell2
```

