# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        q = deque([root])
        res = []
        while q:
            qlen = len(q)
            level = []
            sumLvl = 0
            for _ in range(qlen):
                node = q.popleft()
                sumLvl += node.val
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None
            res.append(sumLvl/qlen)
        
        return res