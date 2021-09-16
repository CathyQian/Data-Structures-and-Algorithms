Summary:
- recursion (divide and conquer, both dfs and bfs solutions for the same problem)
- 5 edge cases 
- always think about both recursive and iterative solution (esp in-order traversal of binary search tree)

```Python
if not node: #(1, empty tree)
    xxx
elif not node.left and not node.right: #(2, node with out children)
    xxx
elif not node.left and node.right: #(3, node with only left child)
    xxx
elif not node.right and node.left: #(4, node with only right child)
    xxx
else: #(5, node with both children)
    xxx
```
- definition of a tree node

```Python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
```

## Tree Traversal (both recursive and iterative solution)
in-order traversal of a tree
```Python

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive traversal
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right

# iterative traversal (very important template for other problems)
class Solution:
    def inorderTraversal(self, root:TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        cur = root
        res = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

# transformer --- Binary Search Tree Iterator
```

```Python
# level-order traversal, using bfs
# another problem to ask is to return the kth smallest element of the BST
class Solution:
    def levelorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = [root, '#']
        res = []
        while q != ['#']:
            ele = q.pop(0)
            layer = []
            while ele != '#':
                layer.append(ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                ele = q.pop(0)
            q.append('#')
            res.append(layer)
        return res

```

## tree sideview
```Python
"""
Solution 1: recursion
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)

        if len(left) <= len(right):
            return [root.val] + right
        else:
            return [root.val] + right + left[len(right):]

"""
Solution 2: layer by layer scanning of binary tree using breadth-first search and then return the last element of each layer
"""
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return [] 
        
        rlist = []
        q = [root, "#"]
        
        while q != ["#"]:
            ele = q.pop(0)
            layer = []
            while ele != '#':
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                layer.append(ele.val)
                ele = q.pop(0)
            q.append('#') # use '#' to separate layers of trees
            rlist.append(layer[-1])
            
        return rlist

# solution 3: layer by layer, use pre and cur two pointers, but that will change the tree structure
# refer to Populating Next Right Pointers in Each Node I, II 

# Populating Next Right Pointers in Each Node I (perfect Binary Tree)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while head:
            cur = head
            while cur and cur.left: # important condition
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next # not under if statement
            head = head.left
        return root

# Populating Next Right Pointers in Each Node II (not perfect binary tree)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = root
        while q:
            cur = q
            head = pre = Node(0) # head and pre points to the same node
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = cur.left
                if cur.right:
                    pre.next = cur.right
                    pre = cur.right
                cur = cur.next
            q = head.next
        return root
```

## tree symmetry
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution 1: use recursion. The trick part here is you have to use two tree for checking symmetry
# using only one tree is more complicated.
class Solution:   
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSym(root, root)

    def isSym(self,L: TreeNode,R: TreeNode) -> bool:
        if not L and not R: 
            return True
        if L and R and L.val == R.val:
            return self.isSym(L.left, R.right) and self.isSym(L.right, R.left)
        return False

# Solution 2: breadth first search. It's a tree and need to read layer by layer. So it's natural to think
# of BFS. The trick part is since it's checking symmtry, so we need to add in pairs, not from left 
# to right.

""" solution 2: iteratively """

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = [root.left, root.right]
        while q:
            l = q.pop(0)
            r = q.pop(0)
            if not l and not r:
                pass
            elif l and r and l.val == r.val:
                q.append(l.left)
                q.append(r.right)
                q.append(l.right)
                q.append(r.left)
            else:
                return False
        return True

```

## is BST?

```Python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))
  
    def isValidBSTRecu(self, root, low, high):
        if not root:
            return True
        
        return low < root.val and root.val < high \
               and self.isValidBSTRecu(root.left, low, root.val) \
               and self.isValidBSTRecu(root.right, root.val, high)
```

## serialize and deserialize a tree (**)

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        q = [root]
        while q:
            ele = q.pop(0)
            if ele:
                q.append(ele.left)
                q.append(ele.right)
            res.append(str(ele.val) if ele else '#') # need to record all None 
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = data.split(',')

        # define root first
        if vals[0] == '#':
            return None
        else:
            root = TreeNode(int(vals[0]))
        q = [root]
        i = 1
        while i < len(vals):
            ele = q.pop(0)
            if vals[i] != '#':
                ele.left = TreeNode(int(vals[i]))
                q.append(ele.left)
            i += 1
            if vals[i] != '#':
                ele.right = TreeNode(int(vals[i]))
                q.append(ele.right)
            i += 1
        return root
```

## max/min path/sum
Define a global parameter, update in the recursive loop. Please note the returning elements of the helper function is usually root with left child or with right child if they are available while the global parameter needs the root + left child + right child.

```Python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        self.globalmax = - float('inf')
        _ = self.maxPathSumHelper(root)
        return self.globalmax
    
    def maxPathSumHelper(self, root):
        # max path sum start at root
        if root is None:
            return 0
        
        left = max(self.maxPathSumHelper(root.left), 0)
        right = max(self.maxPathSumHelper(root.right), 0)
        
        self.globalmax = max(left + root.val + right, self.globalmax)
        
        return max(left, right) + root.val

```

## min/max depth of a BT
max is easier than min, because maxdepth = max(maxdepth(left), maxdepth(right)) + 1
but mindepth != min(mindepth(left), mindepth(right)) + 1
This is mainly because if a node's left child or right child is None, this branch is not considered in calculating the depth.

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root：
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# BFS 
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = [root, '#']
        minDepth = 1
        while q != ['#']:
            ele = q.pop(0)
            while ele != '#':
                if ele.left is None and ele.right is None: # return when finding the first leaf
                    return minDepth
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                ele = q.pop(0)
            minDepth += 1
            q.append('#')

        return 


# recursion
# min depth != min(min depth of left child, min depth of right child) + 1
# has 2 separate cases that cannot be merged into the recursive call    	    
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        if root.left and root.right:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return min(left, right) + 1
	    
        elif root.left:
            return self.minDepth(root.left) + 1
        
	elif root.right:
            return self.minDepth(root.right) + 1
        
	else:
            return 1
	    
```


## delete node in BST
Recursive method, the key in BST here is to find the replacement element (not necessarily its children!!!)

```Python

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
            # please note the following code is incorrect
            # else:
            #    root.val = root.left.val # this is not the right element to replace
            #    root.left = self.deleteNode(root.left, root.left.val)
        return root
        
```
## recover binary search tree

```Python
# Recover Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):                                               
        cur, prev, drops, stack = root, TreeNode(float('-inf')), [], []        
        while cur or stack:                                                    
            while cur:                                                         
                stack.append(cur)                                              
                cur = cur.left                                                 
            node = stack.pop()                                                 
            if node.val < prev.val: # can maintain drops to hold only two elements --> O(1) space
                drops.append((prev, node))                 
            prev, cur = node, node.right                                       
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val 
```
## binary tree to n-ary tree

```Python
# Path Sum III, find number of path from parent to children which sums up to target value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# divide and conquer

class Solution:
    def pathSum(self, root, sum):
        if not root:
            return 0
        cnt = self.pathSumHelper(root, sum) # this path includes the current node 
        left = self.pathSum(root.left, sum)
        right = self.pathSum(root.right, sum)
        return cnt + left + right

    def pathSumHelper(self, node, total):
        # return number of paths include node and sums up to total
        if not node:
            return 0
        count = 0
        if total == node.val:
            count += 1 # not count = 1 as there may be other path as well
        if node.left: # not else, continue search after found, if node values can be negative
            count += self.pathSumHelper(node.left, total - node.val)
        if node.right: # not else, continue search after found
            count += self.pathSumHelper(node.right, total - node.val)
        return count

# binary tree to n-ary tree (cannot use if else anymore since there are too many children, can use for loop instead or dfs) 

class nArryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = []

class Solution:
    def pathSum(self, root, sum):
        if not root:
            return 0
        cnt = self.pathSumHelper(root, sum) # this path includes the current node 
        for child in root.children:
            cnt += self.pathSum(child, sum)
        return cnt

    def pathSumHelper(self, node, total):
        # return number of paths include node and sums up to total
        if not node:
            return 0
        count = 0
        if total == node.val:
            count += 1 # not count = 1 as there may be other path as well
        for child in node.children:
            if child:
                count += self.pathSumHelper(node.left, total - node.val)
        return count


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
```
## all path sum
use dfs

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, '')
    
    def dfs(self, root, path):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            path += str(root.val)
            return int(path)    
        left = self.dfs(root.left, path + str(root.val))
        right = self.dfs(root.right, path + str(root.val))
        return left + right
            

# method 2
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        self.findAllpath(root, '', res)
        pathsum = 0
        for s in res:
            pathsum += int(s)
        return pathsum
    
    def findAllpath(self, node, path, res):
        if node is None:
            return
        if node.left is None and node.right is None:
            res.append(path + str(node.val))
        if node.left:
            self.findAllpath(node.left, path + str(node.val), res)
        if node.right:
            self.findAllpath(node.right, path + str(node.val), res)
```
## distance between two nodes in a binary tree

```Python
# ref: https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/
# method 1: time complexity O(n)

# binary tree node 
class TreeNode: 
    # Constructor to create new node 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None

class Solution: 
    def findDistance(self, root, n1, n2):
        lca = self.LCA(root, n1, n2) 
        if lca:  
            return findDist(lca, n1, 0) + findDist(lca, n2, 0)  
        return -1

    def findDist(self, root, value, dist): # a little tricky, but correct
        if not root: 
            return 0

        if root.data == value: 
            return dist

        left = self.findDist(root.left, data, dist + 1) 
        right = self.findDist(root.right, data, dist + 1) 
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

```
