# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # START
        def pathSum(node, psum):
            if node == None:
                return 0
            psum = psum*10 + node.val

            if node.left == None and node.right == None:
                return psum
            
            return pathSum(node.left, psum) + pathSum(node.right, psum)
        
        return pathSum(root, 0)
