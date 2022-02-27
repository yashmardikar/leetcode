"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque
        if root is None:
            return []
        q = deque([root])
        res = []
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                for child in node.children:
                    q.append(child) if child else None
                level.append(node.val)
            res.append(level)
        return res
                
                