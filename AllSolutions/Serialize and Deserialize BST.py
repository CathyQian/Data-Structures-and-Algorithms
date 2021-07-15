"""
Serialize and Deserialize BST

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a 
network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need
to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

"""

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
        if not root:
            return ""
        q = [root]
        res = []
        while q:
            ele = q.pop(0)
            if ele:
                q.append(ele.left)
                q.append(ele.right)
            res.append(str(ele.val) if ele else '#')
        return ','.join(res)
            

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0:
            return None
        elist = data.split(',')
        root = TreeNode(elist[0])
        q = [root]
        i = 1
        while i < len(elist):
            cur = q.pop(0)
            if elist[i] != '#':
                cur.left = TreeNode(int(elist[i]))
                q.append(cur.left)
            i += 1
            if elist[i] != '#':
                cur.right = TreeNode(int(elist[i]))
                q.append(cur.right)
            i += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
