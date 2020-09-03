"""
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Example 1:
Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""

# Solution: in-order traversal of BST, if no mistake, then the list should be a sorted increasing list. However, a pair of elements is exchanged in this sorted list.
# So the solution is to record prev and current value in pair if prev.val < cur.val. When finished, swap the first and last elment in this list.
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):                                               
        cur, prev, drops, stack = root, TreeNode(float('-inf')), [], []        
        while cur or stack:                                                    
            while cur:                                                         
                stack.append(cur)                                              
                cur = cur.left                                                 
            node = stack.pop()                                                 
            if node.val < prev.val: 
                drops.append((prev, node))                 
            prev, cur = node, node.right                                       
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val 