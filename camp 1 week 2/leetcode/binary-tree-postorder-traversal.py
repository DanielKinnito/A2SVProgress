# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self,node,ans):
            if node is None:
                return None

            self.postorder(node.left,ans) # Left 
            self.postorder(node.right,ans) # Right
            ans.append(node.val) # Root
            
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        self.postorder(root, answer)

        return answer