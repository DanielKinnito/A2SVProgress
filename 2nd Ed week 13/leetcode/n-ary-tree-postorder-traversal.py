"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        answer = []

        def dfs(root):
            for node in root.children:
                dfs(node)
            answer.append(root.val)

        dfs(root)

        return answer