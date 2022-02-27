# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.max_level = float("-inf")
        self.recur(root, level= 1)
        return self.max_level
    
    def recur(self, node, level):
        if node.left is None and node.right is None:
            self.max_level = max(self.max_level, level)
        self.recur(node.left, level+1 ) if node.left else None
        self.recur(node.right, level+1 ) if node.right else None
            