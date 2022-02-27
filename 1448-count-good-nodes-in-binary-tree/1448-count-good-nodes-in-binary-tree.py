# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.goodNodes = 0
        self.recur(root, prev = float("-inf"))
        return self.goodNodes 
    
    def recur(self, root, prev):
        if root:
            if root.val >= prev:
                self.goodNodes += 1
                prev = root.val
            self.recur(root.left, prev) if root.left else None
            self.recur(root.right, prev) if root.right else None