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
                if node.left is not None and node.val >=low:
                    #dont visit left in node val is less than low, 
                    #so all left vals be lower than low
                    q.append(node.left)
                if node.right is not None and node.val <= high:
                    #dont check right as this subtree will contain vals gt high
                    q.append(node.right)
        return res
                
                