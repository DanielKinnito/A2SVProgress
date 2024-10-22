# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        que = deque()
        sums = []
        que.append(root)

        while que:
            size = len(que)
            cur_sum = 0
            for _ in range(size):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                
                cur_sum += node.val
            sums.append(cur_sum)

        if k > len(sums):
            return -1
        sums.sort()
        return sums[-k]    