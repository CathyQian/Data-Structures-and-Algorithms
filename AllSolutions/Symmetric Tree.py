"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around
 its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""
""" solution 1: recursion """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution 1: use recursion. The trick part here is you have to use two tree for checking symmetry
# using only one tree is more complicated.
class Solution:   
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isSym(root, root)

    def isSym(self,L,R):
        if not L and not R: return True
        if L and R and L.val == R.val:
            return self.isSym(L.left, R.right) and self.isSym(L.right, R.left)
        return False

# Solution 2: breadth first search. It's a tree and need to read layer by layer. So it's natural to think
# of BFS. The trick part is since it's checking symmtry, so we need to add in pairs, not from left 
# to right.

""" solution 2: iteratively """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        elif root.left is None and root.right is None:
            return True
        q = [root.left, root.right]
        while q:
            l = q.pop(0)
            r = q.pop(0)
            if l is None and r is None:
                pass
            elif l is not None and r is not None and l.val == r.val:
                q.append(l.left)
                q.append(r.right)
                q.append(l.right)
                q.append(r.left)
            else:
                return False
        return True
