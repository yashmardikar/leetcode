# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])
        res = []
        while q:
            qlen = len(q)
            level = []
            for _ in range(qlen):
                node = q.popleft()
                level.append(node.val)
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None
            res.append(level)
        
        #print(res)
        return res[::-1]