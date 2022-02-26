# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lst = []
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.recur_tree(root)
        new_root = node = TreeNode(self.lst[0])
        for i in range(1, len(self.lst)):
            node.right = TreeNode(self.lst[i])
            node = node.right
        return new_root
        
    def recur_tree(self, root):
        if root:
            self.recur_tree(root.left)
            self.lst.append(root.val)
            self.recur_tree(root.right)
        