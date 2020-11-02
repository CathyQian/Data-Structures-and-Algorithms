"""
Find the next leaf

https://leetcode.com/discuss/interview-question/algorithms/124645/return-the-next-leaf-node-in-tree

Given a tree, if query a leaf node, return the next leaf node. If the queried node is an internal node, return whatever you want. You can define the node structure. (Not a binary tree)

Example:

            a    
        w        x      
     z  y      o   b

If I query 'z' return 'y'. If I query 'y', return 'o'. If I query 'b', return null.

"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def nextLeaf(self, root:TreeNode, target:TreeNode) -> TreeNode:
        if not root or not target:
            return None
        q = []
        pre, cur = None, root
        while q or cur:
            while cur:
                q.append(cur)
                cur = cur.left
            cur = q.pop()
            if pre.val == target.val:
                if pre.left or pre.right: # if pre is internal
                    return pre.left or pre.right 
                else: # if pre in a leaf, return next leaf
                    if not cur.left and not cur.right:
                        return cur
            else:
                pre, cur = cur, cur.right
        return None # if target is the last leave without next node
            
            
                