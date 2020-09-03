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


# ------------------------------------------------------------------------------------------------
# A complete coding question and answer from scratch
"""
BST Successor Search

In a Binary Search Tree (BST), an Inorder Successor of a node is defined as the node with the smallest key 
greater than the key of the input node (see examples below). Given a node inputNode in a BST, you’re asked 
to write a function findInOrderSuccessor that returns the Inorder Successor of inputNode. If inputNode has 
no Inorder Successor, return null.

Explain your solution and analyze its time and space complexities.

In this diagram, the inorder successor of 9 is 11 and the inorder successor of 14 is 20.

Example:
In the diagram above, for inputNode whose key = 11
Your function would return:
The Inorder Successor node whose key = 12

Constraints:
    [time limit] 5000ms
    [input] Node inputNode
    [output] Node
"""

#########################################################
# CODE INSTRUCTIONS:                                    #
# 1) The method findInOrderSuccessor you're asked      #
#    to implement is located at line 30.                #
# 2) Use the helper code below to implement it.         #
# 3) In a nutshell, the helper code allows you to       #
#    to build a Binary Search Tree.                     #
# 4) Jump to line 88 to see an example for how the      #
#    helper code is used to test findInOrderSuccessor.  #
#########################################################


# A node 
class Node:

  # Constructor to create a new node
    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None
        self.parent = None # This is different from most Tree Node definition

# A binary search tree 
class BinarySearchTree:

    # Constructor to create a new BST
    def __init__(self): # root is the key to get access to a BST
        self.root = None 

    def find_in_order_successor(self, inputNode):
        if inputNode.right:
            cur = inputNode.right
            while cur.left:
                cur = cur.left
            return cur
        else: 
            return inputNode.parent
  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid 
  # using reference parameters)
    def insert(self, key):
        # 1) If tree is empty, create the root
        if (self.root is None):
            self.root = Node(key)
        return
        
        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)
        while(currentNode is not None):
            if(key < currentNode.key):
                if(currentNode.left is None):
                    currentNode.left = newNode
                    newNode.parent = currentNode
                break
                else:
                    currentNode = currentNode.left
            else:
                if(currentNode.right is None):
                    currentNode.right = newNode
                    newNode.parent = currentNode
                break
                else:
                    currentNode = currentNode.right

  # Return a reference to a node in the BST by its key.
  # Use this method when you need a node to test your
  # findInOrderSuccessor function on
    def getNodeByKey(self, key):
        currentNode = self.root
        while(currentNode is not None):
            if(key == currentNode.key):
                return currentNode
        
        if(key < currentNode.key):
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right
        
        return None
        
######################################### 
# Driver program to test above function #
#########################################

# Create a Binary Search Tree
bst  = BinarySearchTree()
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);  
bst.insert(14);    

# Get a reference to the node whose key is 9
test = bst.getNodeByKey(20)

# Find the in order successor of test
succ = bst.find_in_order_successor(test)

# Print the key of the successor node
if succ is not None:
    print ("\nInorder Successor of %d is %d " \
            %(test.key , succ.key))
else:
    print ("\nInorder Successor doesn't exist")



# ------------------------------------