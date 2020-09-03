"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """ incorrect, but easy to make mistake
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        if root.left:
            if root.left.val < root.val and self.isValidBST(root.left):
                pass
            else:
                return False
        
        if root.right:
            if root.right.val > root.val and self.isValidBST(root.right):
                pass
            else:
                return False
        
        return True
    """
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))
  
    def isValidBSTRecu(self, root, low, high):
        if root is None:
            return True
        
        return low < root.val and root.val < high \
               and self.isValidBSTRecu(root.left, low, root.val) \
               and self.isValidBSTRecu(root.right, root.val, high)