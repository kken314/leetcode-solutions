# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node: return 0
            return 1 + max(depth(node.left), depth(node.right))
        def good_BST(node):
            if not node: return True
            if abs(depth(node.left) - depth(node.right)) > 1:
                return False
            return good_BST(node.left) and good_BST(node.right)
        return good_BST(root)