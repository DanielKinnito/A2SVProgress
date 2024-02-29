# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
        we can know the ancestor if we can or cannot branch from it. 
    """
    def ancestor(self, root, p, q):
        if root.val > p.val and root.val > q.val:
            return self.ancestor(root.left, p,q)
        elif root.val < p.val and root.val < q.val:
            return self.ancestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.ancestor(root.left, p,q)
        elif root.val < p.val and root.val < q.val:
            return self.ancestor(root.right, p, q)
        else:
            return root