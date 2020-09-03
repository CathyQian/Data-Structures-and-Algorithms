"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum
equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""
"""
solution: similar to Path Sum, use dfs to find all possible rounts
the difference is path needs to be returned here while True/False is the
only concern in Path Sum. So we need a separate recursion here to record the path.

pathSumHelper for dfs, no return because result is a global parameter that is
dynamically changed along the iterations.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        result = []
        self.pathSumHelper(root, sum, [], result)
        
        return result

    def pathSumHelper(self, root, sum, curr, result):
        
        if root is None:
            return 
        
        sum -= root.val
        
        if sum == 0 and root.left is None and root.right == None:
            curr.append(root.val)
            result.append(curr)
        
        if root.left:
            self.pathSumHelper(root.left, sum, curr + [root.val], result) # curr + [root.val] not curr.append(root.val) since python append returns None
        
        if root.right:
            self.pathSumHelper(root.right, sum, curr + [root.val], result)
        
        return