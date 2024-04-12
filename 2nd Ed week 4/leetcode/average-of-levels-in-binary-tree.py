# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        answer = []
        que = deque()
        que.append(root)
        
        while que:
            size = len(que)
            temp_sum = 0
            
            for node in que:
                temp_sum += node.val

            answer.append(temp_sum / size)

            for _ in range(size):
                node = que.popleft()

                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
        
        return answer