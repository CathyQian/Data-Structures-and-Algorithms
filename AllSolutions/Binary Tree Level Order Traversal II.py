"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
"""
solution: bfs from top to bottom, then return reversed list
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
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
        return rlist[::-1]
        
       
