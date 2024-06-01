class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        
        que = deque()
        que.append(root)

        level = 0
        while que:
            length = len(que)
            for _ in range(length):
                node = que.popleft()
                for child in node.children:
                    que.append(child)
            level += 1
        
        return level