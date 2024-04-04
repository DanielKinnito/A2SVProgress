# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node):
            if not node:
                return
            if node.val in check:
                if node.left: answer.append(node.left)
                if node.right: answer.append(node.right)
            
            dfs(node.left)
            dfs(node.right)
        
        def sever(node):
            if not node:
                return
            
            sever(node.left)
            if node.left and node.left.val in check:
                node.left = None
            sever(node.right)
            if node.right and node.right.val in check:
                node.right = None                
        
        check = set(to_delete)
        answer = []
        if not root.val in check:
            answer.append(root)

        dfs(root)
        sever(root)
        
        temp = set(answer)
        for node in answer:
            if node.val in check:
                temp.remove(node)
        
        return list(temp)