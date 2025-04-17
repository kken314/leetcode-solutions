# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            swap(node.right)
            swap(node.left)
        swap(root)
        return root