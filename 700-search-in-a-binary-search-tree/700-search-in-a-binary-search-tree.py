# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.val = val
        if root is None:
            return None
        return self.recur(root)
    
    def recur(self, root):
        if root.val == self.val or root is None:
            return root
        left = self.recur(root.left) if root.left else None
        right = self.recur(root.right) if root.right else None
        if left is not None:
            return left
        else:
            return right
    