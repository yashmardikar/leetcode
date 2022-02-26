# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        from collections import deque
        q = deque([root]) 
        res = 0
        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node.val >= low and node.val <= high:
                    res += node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return res
                
                