# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # START
        '''
        How to use self: https://www.jianshu.com/p/d8735e050047
        https://www.cnblogs.com/ydf0509/p/9435677.html
        Treat self as PUBLIC statement
        '''
        if root == None:
            return True
        
        return self.isSame(root.left, root.right)
    
    def isSame(self, leftnode, rightnode):
        if leftnode ==  None and rightnode == None:
            return True

        if (leftnode ==  None and rightnode != None) or (leftnode !=  None and rightnode == None):
            return False
        
        if leftnode.val != rightnode.val:
            return False

        return self.isSame(leftnode.left, rightnode.right) and self.isSame(leftnode.right, rightnode.left)
