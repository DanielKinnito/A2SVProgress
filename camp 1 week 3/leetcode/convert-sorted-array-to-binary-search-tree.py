# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None

            middle = (left + right) //2
            root = TreeNode(nums[middle])
            root.left = helper(left, middle - 1)
            root.right = helper(middle + 1, right)
            return root

        return helper(0, len(nums) - 1)