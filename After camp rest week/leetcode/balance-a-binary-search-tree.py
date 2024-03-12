# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        
        inorder(root)

        def buildBST(left, right):
            if left > right:
                return None
            
            middle = (left + right) // 2
            return TreeNode(nums[middle], buildBST(left, middle - 1), buildBST(middle + 1, right))
        
        return buildBST(0, len(nums) - 1)