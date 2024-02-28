# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: # Base
            return
        
        if root.val == key: # If key is found
            if root.right: # and that node has a right child
                replace, root = root, root.right
                #Replace inorder successor with node and delete
                while root and root.left:
                    root = root.left
                root.left = replace.left
                
                return replace.right
            
            elif root.left: # else if node has left child 
                return root.left
            
            else:
                return 
        
        elif root.val < key: # Traverse
            root.right = self.deleteNode(root.right, key)
        
        else: # Traverse
            root.left = self.deleteNode(root.left, key)   
        
        return root