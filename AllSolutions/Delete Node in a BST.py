"""
Given a root node reference of a BST and a key, delete the node with the given
key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""
"""
Solution: dfs, replace root node with the most left node from the right child, then
delete that node using recursion.
节点没有左子树：返回其右子树
节点没有右子树：返回其左子树
既有左子树，又有右子树： 
1）查找到其右子树的最小值的节点，替换掉被删除的节点，并删除找到的最小节点 
or 2）查找到其左子树的最大值的节点，替换掉被删除的节点，并删除找到的最大节点
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
            
        if root is None:
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        else: # root.val == key, keep using recursion and consider 5 conditions here
            if root.left is None:
                return root.right
            
            elif root.right is None:
                return root.left
            
            else: # both left and right are not None
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val) # good use of recursion
                
        return root
        