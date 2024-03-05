# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root, least, most):
            if not root:
                return float('-inf')
            least = min(least, root.val)
            most = max(most, root.val)

            left = helper(root.left, least, most)
            right = helper(root.right, least, most)

            return max(most - least, max(left, right))
        
        return helper(root, float('inf'), float('-inf'))