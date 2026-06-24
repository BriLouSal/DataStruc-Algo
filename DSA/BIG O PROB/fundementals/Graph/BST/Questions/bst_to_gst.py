# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Find the binary serach tree  for greater sum, Every key original BST
        # is changed Orignal PLUS the sum of all keys greater than original key iN BST
        # so for example 4 = 6 + 7 + 5 + 8  + 4 (Add itself)
        # So we calculate via the right side of that nodes and add the number to itself
        self.sum_of_node = 0
        # Create a function that we can do to tranverse through the nodes and find CALCULATE the right side of the nodes
        def transverse_nodes(node):
            if not node:
                return
            #  4 -> 6 nodes
            transverse_nodes(node.right)
            # Add the value of itself
            self.sum_of_node += node.val
            node.val = self.sum_of_node
            transverse_nodes(node.left)
        transverse_nodes(root)
        return root

