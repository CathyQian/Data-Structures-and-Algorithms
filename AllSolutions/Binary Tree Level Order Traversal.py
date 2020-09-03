"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to 
right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: # need to take this out as an edge case, [[]] is not None, [] is None
            return []
        rlist = []
        q = [root]
        while q and q != ['#']:
            q.append('#')
            r = []
            ele = q.pop(0)
            while ele and ele != '#':
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                r.append(ele.val)
                ele = q.pop(0)
            rlist.append(r)
        return rlist