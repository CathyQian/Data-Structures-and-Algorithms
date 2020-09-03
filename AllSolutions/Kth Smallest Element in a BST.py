"""
Given a binary search tree, write a function kthSmallest to find the kth smallest
element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find
the kth smallest frequently? How would you optimize the kthSmallest routine?
"""
"""
注意定义:
二叉排序树(Binary Search Tree)又称二叉搜索(查找)树，其定义如下：
(1) 若它的左子树非空，则左子树上所有结点的权值都比根结点的权值小;
(2) 若它的右子数非空，则右子树上所有结点的权值都比根结点的权值大;
(3) 左、右子树本身又是一棵二叉排序树。
因此采用中序遍历（左 -> 根 -> 右）即可以递增顺序访问BST中的节点，从而得到第k小的元素，时间复杂度O(k)
Follow up: need to remember the value of the kth and (k-1)th smallest element,
if the inserted is the bigger than the kth, return the kth; if smaller, return
the (k-1) the smallest element
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while root != None:
            stack.append(root)
            root = root.left
        while stack:
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            if curr.right:
                curr = curr.right
                while curr:
                    stack.append(curr)
                    curr = curr.left
