"""
Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: # edge case
            return None
        res = []
        q = [root, '#']
        flag = 1
        while q !=  ['#']:
            ele = q.pop(0)
            layer = []
            while ele != '#':
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                layer.append(ele.val) # return ele.val not ele
                ele = q.pop(0)
            q.append('#')
            if flag == -1:
                res.append(layer[::-1])
            else:
                res.append(layer)
            flag *= -1
        return res