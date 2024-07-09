class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if not root:
            return []

        que = deque()
        que.append(root)

        while que:
            length = len(que)
            for i in range(length):
                node = que.popleft()

                if i == length - 1:
                    answer.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        
        return answer