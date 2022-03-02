# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        return self.recur(root, low, high)
    
    def recur(self, root, low, high):
        if root is None:
            return 0
        if low<= root.val <= high:
            leftVal = self.recur(root.left, low, high) if root.left else 0
            rightVal = self.recur(root.right, low, high) if root.right else 0
            return root.val + leftVal + rightVal
        
        if root.val > high:
            leftVal = self.recur(root.left, low, high) if root.left else 0
            return leftVal
        if root.val < low:
            rightVal = self.recur(root.right, low, high) if root.right else 0
            return rightVal