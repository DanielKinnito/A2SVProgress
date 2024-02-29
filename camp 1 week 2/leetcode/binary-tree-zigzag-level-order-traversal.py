# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        dictionary = defaultdict(list)
        def helper(root, index):
            if not root:
                return None
            dictionary[index].append(root.val)
            helper(root.left, index + 1)
            helper(root.right, index + 1)
            
            return root
        
        helper(root,0)

        answer = []
        for i in range(len(dictionary)):
            answer.append(dictionary.get(i))
        
        for i in range(len(answer)):
            if i % 2 != 0:
                answer[i] = answer[i][::-1]
        
        return answer