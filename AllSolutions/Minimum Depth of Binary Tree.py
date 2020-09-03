"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS 
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = [root]
        minDepth = 1
        while q and q != ['#']:
            q.append('#')
            ele = q.pop(0)
            while ele and ele != '#':
                if ele.left is None and ele.right is None: 
                    return minDepth
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                ele = q.pop(0)
            minDepth += 1
        return 



# recursion
# min depth = min(min depth of left child, min depth of right child) + 1

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        elif root.left is None and root.right is None:
            return 1
        
        elif root.left is not None and root.right is None:
            left = self.minDepth(root.left)
            return left + 1
        
        elif root.right is not None and root.left is None:
            right = self.minDepth(root.right)
            return right + 1
        
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return min(left, right) + 1