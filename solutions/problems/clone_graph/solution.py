"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        OldToNew = {}
        
        def DFS(node):
            if node in OldToNew:
                return OldToNew[node]
            OldToNew[node] = Node(node.val)
            for nei in node.neighbors:
                OldToNew[node].neighbors.append(DFS(nei))
            return OldToNew[node]
        return DFS(node)
