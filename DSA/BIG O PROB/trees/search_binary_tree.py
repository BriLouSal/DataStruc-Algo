# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Like Linked list we have to return None in order to make our algo efficent, beceause it'd be not that good if we just do it even though
        # we know there's nothing in it
        if not root:
            return None
        
        # Let's use the iterative approach

        current = root
        while  current:
            # So if the current.val is equal to the val then we found the TreeNode
            if current.val == val:
                return current
            # And then we iterate through the BST and use the rule right so if the val is less than the current.val, we would check the left
            
            if val < current.val:
                current = current.left
                
            # But if not we go to the right, so we keep doing that until find the current.val is equal to the val, if not we get None
            else:
                current = current.right
        return None