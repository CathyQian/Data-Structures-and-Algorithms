class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        while root:
            if root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
            else:
                return root
        
        return root