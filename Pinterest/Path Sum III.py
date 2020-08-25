"""
Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from
parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):

        # divide and conquer
        if not root:
            return 0
        cnt = self.pathSumHelper(root, sum) # make sure in pathSumHelper the path includes the current node 
        left = self.pathSum(root.left, sum)
        right = self.pathSum(root.right, sum)
        return cnt + left + right

    def pathSumHelper(self, node, total):
        if not node:
            return 0
        count = 0
        if total == node.val:
            count += 1
        if node.left: # not else, continue search after found
            count += self.pathSumHelper(node.left, total - node.val)
        if node.right: # not else, continue search after found
            count += self.pathSumHelper(node.right, total - node.val)
        return count

# binary tree to n-ary tree
import collections
class nArryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = []

class Solution:
    def pathSum(self, root, target):
        if not root:
            return 0
        self.result = 0
        self.memo = collections.defaultdict(int)
        self.memo[0] = 1
        self.dfs(root, 0, target)
        return self.result
    
    def dfs(self, root, cursum, target):
        if root:
            cursum += root.val
            residual = cursum - target
            self.result += self.memo[residual]
            # do dfs starting from the path include root
            self.memo[cursum] += 1
            for node in root.children: # change these into left chile or right child, can be applied to binary tree case
                self.dfs(node, cursum, target)
            # finish dfs starting from root, remove the cursum ending in this root
            # since we can't use them in other path
            self.memo[cursum] -= 1 # critical

leaf1 = nArryTreeNode(3)
leaf2 = nArryTreeNode(8)
leaf3 = nArryTreeNode(4)
leaf4 = nArryTreeNode(5)
leaf5 = nArryTreeNode(8)
leaf6 = nArryTreeNode(5)
mid1 = nArryTreeNode(5)
mid2 = nArryTreeNode(4)
mid3 = nArryTreeNode(3)
root = nArryTreeNode(8)
root.children = [mid1, mid2, mid3]
mid1.children = [leaf1]
mid2.children = [leaf2, leaf3]
mid3.children = [leaf4, leaf5, leaf6]

test = Solution()
print(test.pathSum(root, 8))