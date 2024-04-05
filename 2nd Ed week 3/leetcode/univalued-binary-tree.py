class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        compare = root.val

        que = deque()
        que.append(root)

        while que:
            node = que.popleft()

            if node.left: 
                if node.left.val != compare:
                    return False
                que.append(node.left)
            if node.right: 
                if node.right.val != compare:
                    return False
                que.append(node.right)
        
        return True