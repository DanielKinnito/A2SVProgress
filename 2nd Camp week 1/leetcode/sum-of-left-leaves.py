class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node, flag, val):
            nonlocal answer
            
            if not node.left and not node.right and flag:
                answer += val

            if node.left:
                dfs(node.left, True, node.left.val)
            
            if node.right:
                dfs(node.right, False,0)
        
        dfs(root, False, 0)
        return answer