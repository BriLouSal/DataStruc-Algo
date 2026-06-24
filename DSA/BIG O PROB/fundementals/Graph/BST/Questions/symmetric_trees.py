# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # We can split them appart via the middle and check if it's valid or aka True
        if root is None:
            return None
        def mirror_timberlake(left_node, right_node):
            # Tree is empty
            if  not left_node and not right_node:
                return True
            if not left_node or not right_node or left_node.val != right_node.val:
                return False
            return mirror_timberlake(left_node.left, right_node.right) and  mirror_timberlake(left_node.right, right_node.left)
        return mirror_timberlake(root.left, root.right)
 



        