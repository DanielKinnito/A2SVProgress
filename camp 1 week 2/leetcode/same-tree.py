# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        return p.val == q.val and self.traverse(p.left, q.left) and self.traverse(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverse(p,q)