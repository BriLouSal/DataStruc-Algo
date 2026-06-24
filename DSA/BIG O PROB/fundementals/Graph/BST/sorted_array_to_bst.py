# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # So using this idea we have to check if the middle value we can 
        # do this and then let that be centre of the of the array
        if not nums:
            return None

        middle =  len(nums) // 2
        node = TreeNode(nums[middle])
        # Left side will go with the x > middle 
        node.left = self.sortedArrayToBST(nums[:middle])
        node.right = self.sortedArrayToBST(nums[middle + 1:])
        return node