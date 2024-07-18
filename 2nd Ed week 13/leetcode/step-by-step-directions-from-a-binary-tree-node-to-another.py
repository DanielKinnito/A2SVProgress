# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_path(node, target, path):
            if not node:
                return False
            
            if node.val == target:
                return True
            
            path.append('L')
            if find_path(node.left, target, path):
                return True
            path.pop()
            
            path.append('R')
            if find_path(node.right, target, path):
                return True
            path.pop()
            
            return False

        path_to_start = []
        path_to_dest = []
        
        find_path(root, startValue, path_to_start)
        find_path(root, destValue, path_to_dest)

        i = 0
        while i < len(path_to_start) and i < len(path_to_dest) and path_to_start[i] == path_to_dest[i]:
            i += 1

        steps_up = 'U' * (len(path_to_start) - i)
        steps_down = ''.join(path_to_dest[i:])

        return steps_up + steps_down