# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        temp = []

        que = deque()
        que.append(root)

        while que:
            level = len(que)
            for _ in range(level):
                node = que.popleft()
                temp.append(node.val)

                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
        
        temp.sort()
        answer = inf
        for i in range(1, len(temp)):
            answer = min(answer, temp[i] - temp[i - 1])

        return answer