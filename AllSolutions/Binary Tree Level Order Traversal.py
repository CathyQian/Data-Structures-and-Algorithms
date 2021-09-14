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

# bfs solution
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: # need to take this out as an edge case, [[]] is not None, [] is None
            return []
        rlist = []
        q = [root, '#']
        while q and q != ['#']:
            r = []
            ele = q.pop(0)
            while ele and ele != '#':
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                r.append(ele.val)
                ele = q.pop(0)
            q.append('#')
            rlist.append(r)
        return rlist

 # dfs solution
 class Solution:
     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # DFS recursively 
         ret = []
         self.helper(root, 0, ret)
         return ret         
        
     def helper(self, root, level, ret):
         if root:
             if len(ret) < level+1:
                 ret.append([ ]) 
             ret[level].append(root.val)
             self.helper(root.left,  level+1, ret)   
             self.helper(root.right, level+1, ret) 
            
 
