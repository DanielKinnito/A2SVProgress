# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from statistics import mode
class Solution:
    def traverse(self, root, array):
        if not root:
            return None
        self.traverse(root.left, array)
        array.append(root.val)
        self.traverse(root.right, array)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        self.traverse(root, array)
        
        frequencies = {}
        for num in array:
            frequencies[num] = frequencies.get(num, 0) + 1

        max_frequency = max(frequencies.values())
        modes = [key for key, value in frequencies.items() if value == max_frequency]

        return modes