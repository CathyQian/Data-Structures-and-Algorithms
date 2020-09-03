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
        lca = LCA(root, n1, n2) 
        d1, d2 = [], []
        if lca:  
            findLevel(lca, n1, d1, 0)
            findLevel(lca, n2, d2, 0) 
            return d1[0] + d2[0] 
        else: 
            return -1

    def findLevel(self, root, value, d, level): 
        if not root: 
            return

        if root.data == value: 
            d.append(level)
            return

        findLevel(root.left, data, d, level + 1) 
        findLevel(root.right, data, d, level + 1) 

    def LCA(self, root, n1, n2): 
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
