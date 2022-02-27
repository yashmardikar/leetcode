# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            self.min_level = float("inf")
            self.recur(root, level = 0)
            return self.min_level
        else:
            return 0
    
    def recur(self, root, level):
        level += 1
        if level < self.min_level:
            #keep exploring only if existing level < min_level
            self.recur(root.left, level) if root.left else None
            self.recur(root.right, level) if root.right else None
            if root.left is None and root.right is None and level < self.min_level:
                self.min_level = min(self.min_level, level)
                self.min_level = level
        