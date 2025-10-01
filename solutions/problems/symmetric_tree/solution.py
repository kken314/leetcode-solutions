# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(LeftTree, RightTree):
            if not LeftTree and not RightTree: return True
            if not LeftTree or not RightTree: return False 

            return (LeftTree.val == RightTree.val) and isMirror(LeftTree.left, RightTree.right) and isMirror(LeftTree.right, RightTree.left)
        
        return isMirror(root.left, root.right)