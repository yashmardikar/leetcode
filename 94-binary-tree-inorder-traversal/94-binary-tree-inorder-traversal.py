# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self. lst = []
        self.inorder_recur(root)
        return self.lst
    
    def inorder_recur(self, root):
        if root:
            self.inorder_recur(root.left) if root.left else None
            self.lst.append(root.val)
            self.inorder_recur(root.right) if root.right else None
    