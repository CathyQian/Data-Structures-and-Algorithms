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
5. Check my algorithm notes

