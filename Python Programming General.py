# class
class Dog: # class name
    # class attributes
    attr1 = 'dog'
    attr2 = 'mamal'

    # init method or constructor (used to initialize the object's state)
    def __init__(self, name):
        self.name = name
    
    # method
    def say_hi(self):
        print('Hello, my name is', self.name)


# object instantiation
Rodger = Dog('Robin')

# access class attributes
print(Rodger.attr1)

# access class method
Rodger.say_hi()

# Leetcode solution (https://leetcode.com/problems/validate-binary-search-tree/)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None): # initialize tree node to be None
        self.val = val
        self.left = left
        self.right = right

# define solution
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        minval, maxval = -sys.maxsize, sys.maxsize
        return self.isValidBSTHelper(root, minval, maxval)
    
    def isValidBSTHelper(self, root, minval, maxval):
        if not root:
            return True
        if root.val > minval and root.val < maxval:
            return self.isValidBSTHelper(root.left, minval, root.val) and self.isValidBSTHelper(root.right, root.val, maxval)

            