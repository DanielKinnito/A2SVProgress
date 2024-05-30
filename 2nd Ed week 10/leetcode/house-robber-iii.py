class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dp(node):
            if not node:
                return 0, 0

            left = dp(node.left)
            right = dp(node.right)
            
            take = node.val + left[0] + right[0]
            leave = max(left) + max(right)
            
            return leave, take
        
        return max(dp(root))