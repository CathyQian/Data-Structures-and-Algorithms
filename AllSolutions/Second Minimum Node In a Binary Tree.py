"""
Second Minimum Node In a Binary Tree

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.

 

Constraints:

    The number of nodes in the tree is in the range [1, 25].
    1 <= Node.val <= 231 - 1
    root.val == min(root.left.val, root.right.val) for each internal node of the tree.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution():
    def findSecondMinimumValue(self, root):
        res = [float('inf')]
        def traverse(node):
            if not node:
                return
            if root.val < node.val < res[0]:
                res[0] = node.val
            if node.left and node.left.val < res[0]:
                traverse(node.left)
            if node.right and node.right.val < res[0]:
                traverse(node.right)
        traverse(root)
        return -1 if res[0] == float('inf') else res[0]