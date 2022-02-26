# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def postorder(node):
            nonlocal res
            if not node:
                return
            postorder(node.left) if node.val >= low else None
            postorder(node.right) if node.val <= high else None
            if low <= node.val <= high:
                res += node.val
            
        postorder(root)
        return res