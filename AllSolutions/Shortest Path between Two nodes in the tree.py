# ref: https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/
# method 1: time complexity O(n)

""" 
A python program to find distance between n1 
and n2 in binary tree 
"""
# binary tree node 
class Node: 
    # Constructor to create new node 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None

class Solution: 
    def findDistance(self, root, n1, n2): 
        lca = self.LCA(root, n1, n2) 
        if lca:  
            return findLevel(lca, n1, 0) + findLevel(lca, n2, 0)  
        return -1

    def findLevel(self, root, value, level): 
        if not root: 
            return 0

        if root.data == value: 
            return level + 1

        left = findLevel(root.left, data, level + 1) 
        right = findLevel(root.right, data, level + 1) 
	return max(left, right)

    def LCA(self, root, n1, n2): 
	# lowest common ancestor
        if not root: 
            return None
        if root.val == n1 or root.val == n2: 
            return root 
    
        left = self.LCA(root.left, n1, n2) 
        right = self.LCA(root.right, n1, n2) 

        if not left and not right: 
            return root 

        if left: 
            return left 
        else: 
            return right 
