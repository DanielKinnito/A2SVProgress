# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,node,array):
            if node is None:
                return None

            self.inorder(node.left,array) # Left 
            array.append(node.val) # Root
            self.inorder(node.right,array) # Right
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        array = []
        self.inorder(root, array)
        low_idx = 0
        high_idx = 0

        for i in range(len(array)):
            if array[i] == low:
                low_idx = i
            if array[i] == high:
                high_idx = i
        
        answer = sum(array[low_idx: high_idx + 1])
        return answer