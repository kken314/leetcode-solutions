# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        found = False
        def DFS(node):
            nonlocal found
            if not node or found:
                return
            DFS(node.left)
            inorder.append(node.val)
            if len(inorder) == k:
                found = True
            DFS(node.right)
        DFS(root)
        return inorder[k - 1]
