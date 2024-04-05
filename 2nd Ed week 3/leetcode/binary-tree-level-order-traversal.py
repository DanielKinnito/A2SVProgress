class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        answer = []

        que = deque()
        que.append(root)

        while que:
            temp = []

            size = len(que)
            for _ in range(size):
                node = que.popleft()
                
                temp.append(node.val)

                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            
            answer.append(temp)
        
        return answer