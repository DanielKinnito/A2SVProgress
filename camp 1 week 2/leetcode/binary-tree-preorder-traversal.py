# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,node,ans):
            if node is None:
                return None

            ans.append(node.val) # Root
            self.preorder(node.left,ans) # Left 
            self.preorder(node.right,ans) # Right

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        self.preorder(root, answer) 

        return answer