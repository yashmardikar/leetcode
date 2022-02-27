# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        if root is None:
            return []
        q = deque([root])
        res = []
        reverse = False
        while q:
            qlen = len(q)
            level = []
            reverse = not reverse
            for _ in range(qlen):
                if reverse:
                    node = q.popleft()
                    q.append(node.left) if node.left else None
                    q.append(node.right) if node.right else None
                else:
                    node = q.pop()
                    q.appendleft(node.right) if node.right else None
                    q.appendleft(node.left) if node.left else None
                level.append(node.val)
            res.append(level)
        return res
