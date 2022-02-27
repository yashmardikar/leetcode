# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        q = deque([root])
        res = []
        while q:
            qlen = len(q)
            currMax = float("-inf")
            for _ in range(qlen):
                node = q.popleft()
                currMax = max(currMax, node.val)
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None
            res.append(currMax)
        return res