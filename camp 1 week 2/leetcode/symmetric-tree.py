# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,left, right):
        if (not left and right) or (not right and left):
            return False
        
        if left and right and left.val != right.val:
            return False
        
        if right and left and not self.inorder(right.right, left.left):
            return False
        
        if right and left and not self.inorder(right.left, left.right):
            return False
        
        return True
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.inorder(root, root)