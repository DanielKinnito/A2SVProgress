class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        
        if not root:
            return []

        que = deque()
        que.append(root)

        while que:
            answer.append([node.val for node in que])
            
            size = len(que)
            for _ in range(size):
                node = que.popleft()

                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
        
        return answer