# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,node,ans):
            if node is None:
                return None

            self.inorder(node.left,ans) # Left 
            ans.append(node.val) # Root
            self.inorder(node.right,ans) # Right
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        self.inorder(root, answer)

        return answer