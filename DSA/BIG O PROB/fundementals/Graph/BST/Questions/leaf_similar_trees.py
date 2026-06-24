# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # We only need to look at root 1 and root 2's left and right and if they are equal so this is pretty simple, we just have to tranverse to it 
        left_one = root1.left
        right_one = root1.right

        def tranverse(nodes, list_of):
            if not nodes:
                return None
            if not nodes.left and not nodes.right:
                list_of.append(nodes.val)
            tranverse(nodes.left, list_of)
            tranverse(nodes.right, list_of)
                


        l1 = []
        l2 = []
        tranverse(root1, l1) 
        tranverse(root2, l2)
    

        return l1 == l2

