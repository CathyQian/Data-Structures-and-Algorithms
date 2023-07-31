"""
Step-By-Step Directions From a Binary Tree Node to Another

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start 
node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. 
Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

Example 1:

Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:

Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
"""
"""
Solution 1:
Build directions for both start and destination from the root.
Say we get "LLRRL" and "LRR".
Remove common prefix path.
We remove "L", and now start direction is "LRRL", and destination - "RR"
Replace all steps in the start direction to "U" and add destination direction.
The result is "UUUU" + "RR".
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def find(n: TreeNode, val: int, path: List[str]) -> bool:
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path.append("L")
            elif n.right and find(n.right, val, path):
                path.append("R")
            return True if path else False
        
        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
            
        return "".join("U" * len(s)) + "".join(reversed(d))
    
# solution 2: find lca first, then find path
from collections import deque
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def lca(node): 
            """Return lowest common ancestor of start and dest nodes."""
            if not node or node.val in (startValue , destValue): 
                return node 
            left, right = lca(node.left), lca(node.right)
            return node if left and right else left or right
        
        node = lca(root) # only this sub-tree matters
        ps = pd = ""
        d = deque([(node, "")])
        while d: 
            node, path = d.popleft()
            if node.val == startValue: 
                ps = path 
            if node.val == destValue: 
                pd = path
            if node.left: 
                d.append((node.left, path + "L"))
            if node.right: 
                d.append((node.right, path + "R"))
        return "U"*len(ps) + pd