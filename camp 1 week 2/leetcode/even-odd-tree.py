# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        1. Just like zigzag binary question, go through the tree 
        and put the elements in a dictionary at their depth
        2. Then check if each set of lists satisfy the conditions

        A better way is to not have dictionary at all and go through
        the tree and checking the index and the value. But i dont know 
        how to do that yet.
        I have also seen people use stacks and deques, maybe do that
    """

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        dictionary = defaultdict(list)
        # flag = 
        def helper(root, index):
                if not root:
                    return None
                dictionary[index].append(root.val)
                helper(root.left, index + 1)
                helper(root.right, index + 1)
                
                return root
        
        helper(root,0)

        for i in range(len(dictionary)):
            level = dictionary.get(i)
            for j in range(len(level)):
                if i % 2 == 0 and (level[j] % 2 == 0 or (j > 0 and level[j] <= level[j - 1])):
                    return False
                elif i % 2 == 1 and (level[j] % 2 != 0 or (j > 0 and level[j] >= level[j - 1])):
                    return False

        return True