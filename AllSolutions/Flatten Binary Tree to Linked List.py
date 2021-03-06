"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if root is None:
            pass
        
        elif root.left is None:
            self.flatten(root.right)
        
        else:
            self.flatten(root.left)
            self.flatten(root.right)

            temp = root.right
            
            cur = root.left
            root.right = cur
            while cur and cur.right:
                cur = cur.right
            cur.right = temp
            root.left = None
        
        
        
        