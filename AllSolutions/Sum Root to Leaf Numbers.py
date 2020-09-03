"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        return self.dfs(root, '')
    
    def dfs(self, root, path):
        
        if root is None:
            return 0
        
        elif root.left is None and root.right is None:
            path += str(root.val)
            return int(path)    
        
        left = self.dfs(root.left, path + str(root.val))
        right = self.dfs(root.right, path + str(root.val))
        
        return left + right
            

# method 2
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        self.findAllpath(root, '', res)
        pathsum = 0
        for s in res:
            pathsum += int(s)
        return pathsum
    
    def findAllpath(self, node, path, res):
        if node is None:
            return
        if node.left is None and node.right is None:
            res.append(path + str(node.val))
        if node.left:
            self.findAllpath(node.left, path + str(node.val), res)
        if node.right:
            self.findAllpath(node.right, path + str(node.val), res)