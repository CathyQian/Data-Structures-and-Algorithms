"""
Given a binary tree, imagine yourself standing on the right side of it, return
the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
"""
Solution 1: recursion
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)

        if len(left) <= len(right):
            return [root.val] + right
        else:
            return [root.val] + right + left[len(right):]

"""
Solution 2: layer by layer scanning of binary tree using breadth-first search and then return the last element of each layer
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return [] 
        
        rlist = []
        q = [root, "#"]
        
        while q != ["#"]:
            ele = q.pop(0)
            layer = []
            while ele != '#':
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                layer.append(ele.val)
                ele = q.pop(0)
            q.append('#') # use '#' to separate layers of trees
            rlist.append(layer[-1])
            
        return rlist