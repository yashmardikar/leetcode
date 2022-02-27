# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.lst = []
        self.recur(root)
        mindiff = float("inf")
        for i in range(1, len(self.lst)):
            mindiff = min(self.lst[i] - self.lst[i-1], mindiff)
        return mindiff    
    
    def recur(self, root):
        if root:
            self.recur(root.left) if root.left else None
            self.lst.append(root.val)
            self.recur(root.right) if root.right else None
        
            
            
