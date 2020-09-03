Three types:
1. The main function is recursively used directly without helper recursion function
    - examples: 
    ```python
    # depth of a tree
    def main(root):
        l = self.main(root.left)
        r = self.main(root.right)
        return max(l, r) + 1
    ```
2. Return from recursion function is not used but rather an intermediate stage to update a predefined global parameter which is the return for the main function
    - examples: 
    ```python
    # diameter of a tree
    class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxnodes = 0 # pay attention to the different definition of maxnodes and maxdiameter
        _ = self.diameterHelper(root)
        return max(0, self.maxnodes - 1) # in case it's negative 
                               
    def diameterHelper(self, node):
        # return max # nodes between node-left child and node-right child
        if not node:
            return 0
        l = self.diameterHelper(node.left)
        r = self.diameterHelper(node.right)
        self.maxnodes = max(self.maxnodes, l+r+1) 
                               
        return max(l,r) + 1
    ```
    ```python
    # is binary tree balanced 

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class Solution:
        def isBalanced(self, root: TreeNode) -> bool:
            if not root:
                return True
            return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.height(root.left) - self.height(root.right)) <= 1
        
        def height(self, root):
            if not root:
                return 0
            else:
                return 1 + max(self.height(root.left), self.height(root.right))
    ```
    ```python
    # binary tree longest consecutive sequence
    class Solution:
        def longestConsecutive(self, root: TreeNode) -> int:
            self.maxlength = 0
            self.longestConsecutiveHelper(root, 0)
            return self.maxlength
        
        def longestConsecutiveHelper(self, node, curr_len):
            if not node:
                return
            self.maxlength = max(self.maxlength, curr_len + 1)
            if node.left:
                if node.left.val == node.val + 1:
                    self.longestConsecutiveHelper(node.left, curr_len+1)
                else: # needed for dfs
                    self.longestConsecutiveHelper(node.left, 0)
            if node.right:
                if node.right.val == node.val + 1:
                    self.longestConsecutiveHelper(node.right, curr_len + 1)
                else: # needed for dfs
                    self.longestConsecutiveHelper(node.right, 0)
    ```
3. nested use of recursion function: recursion function and main function are recursively used in the main function multiple times. It's quite easy to get redundancy in the code, i.e., not using the recusive call of the main function correctly.
    - examples:
    ```python
    
    def main(root):
        # solution may or may not include root
        a = self.mainhelper(root)
        b = self.main(root.left)
        c = self.main(root.right)
        return a + b + c
    
    def mainhelper(node):
        # solution starting from node
    ```