# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque([root])
        depth = 0
        while q:
            depth+=1
            qlen = len(q)
            for _ in range(qlen):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return depth
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None
        
                
        