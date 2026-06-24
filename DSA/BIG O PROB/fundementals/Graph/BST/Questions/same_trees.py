# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_list = []
        q_list = []

        def tranpose(node, lists):
            if node is None:
                lists.append(None)
                return 
            lists.append(node.val)
            tranpose(node.right, lists)
            tranpose(node.left, lists)

        tranpose(p, p_list)
        tranpose(q, q_list)
        return p_list == q_list
    
    