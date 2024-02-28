# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def BST(self,root, val):
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.BST(root.left, val)
            return root
        
        if val > root.val:
            root.right = self.BST(root.right, val)
            return root

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.BST(root, val)