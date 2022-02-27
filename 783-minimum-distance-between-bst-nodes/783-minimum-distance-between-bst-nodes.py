# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.mindiff = float("inf")
        self.recur(root)
        return self.mindiff
    
    def recur(self, root):
        if root:
            self.recur(root.left) if root.left else None
            if self.prev is not None:
                self.mindiff = min(self.mindiff, root.val - self.prev )
            self.prev = root.val
            self.recur(root.right) if root.right else None
        
            
            
