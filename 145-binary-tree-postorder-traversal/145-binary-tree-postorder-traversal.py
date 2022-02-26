# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.lst = []
        self.postorder_recur(root)
        return self.lst
    
    def postorder_recur(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.postorder_recur(root.left) if root.left else None
            self.postorder_recur(root.right) if root.right else None
            self.lst.append(root.val)
        