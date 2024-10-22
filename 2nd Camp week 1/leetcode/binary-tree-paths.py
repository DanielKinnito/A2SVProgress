class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        def dfs(node, path):
            if not node:
                return
            
            path.append(str(node.val))
            if not node.left and not node.right:
                answer.append('->'.join(path))
            
            if node.left:
                dfs(node.left, path[::])
            if node.right:
                dfs(node.right, path[::])
        
        dfs(root, [])
        return answer