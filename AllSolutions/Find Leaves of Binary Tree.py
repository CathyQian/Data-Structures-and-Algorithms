"""
Find Leaves of Binary Tree

Given the root of a binary tree, collect a tree's nodes as if you were doing this:

    Collect all the leaf nodes.
    Remove all the leaf nodes.
    Repeat until the tree is empty.

 

Example 1:

Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.

Example 2:

Input: root = [1]
Output: [[1]]


Constraints:

    The number of nodes in the tree is in the range [1, 100].
    -100 <= Node.val <= 100


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution():
    def findLeaves(self, root):
        res = []
        self.order(root, res)
        return res      
    
    def order(self, root, res):
        if not root:
            return -1
        left = self.order(root.left, res)
        right = self.order(root.right, res)
        height = max(left, right) + 1   # max not min
        if height >= len(res): # add the first element
            res.append([root.val])
        else:
            res[height].append(root.val)
        return height