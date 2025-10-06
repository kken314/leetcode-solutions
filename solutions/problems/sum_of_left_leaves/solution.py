# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def SLL(node, LR_state):
            if not node:
                return 0
            if not node.left and not node.right:
                if LR_state == 'L':
                    return node.val
                else:
                    return 0
                return node.left.val
            return SLL(node.left, 'L') + SLL(node.right, 'R') 
        return SLL(root, 'root')