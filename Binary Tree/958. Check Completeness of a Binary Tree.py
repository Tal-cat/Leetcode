# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # STRAT
        '''
        def isComplete(rootnode):
            if rootnode == None:
                return True
            if rootnode.left == None and rootnode.right != None:
                return False
            if rootnode.left != None and rootnode.right = None:
                # Failed, need to access parent node
            else:
                return (isComplete(rootnode.left) and isComplete(rootnode.right))
        
        return isComplete(root)
        '''
        if not root:
            return True
        
        queue = [root]
        flag_null = False

        while queue:
            node = queue.pop(0)
            if node == None:
                flag_null = True
                continue

            if flag_null:
                return False
            
            queue.append(node.left)
            queue.append(node.right)
            
        return True
