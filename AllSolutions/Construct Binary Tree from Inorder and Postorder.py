"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0 or len(postorder) != len(inorder):
            return None
        
        root = TreeNode(postorder[-1])
        split_idx_in = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[:split_idx_in], postorder[:split_idx_in])
        root.right = self.buildTree(inorder[split_idx_in + 1:], postorder[split_idx_in: -1])
        
        return root