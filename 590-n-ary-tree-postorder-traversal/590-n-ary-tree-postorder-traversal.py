"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:        
    def postorder(self, root: 'Node') -> List[int]:
        self.lst = []
        self.postorderTraversal(root)
        return self.lst
        
    def postorderTraversal(self, root: 'Node') -> List[int]:
        if root:
            for child in root.children:
                if child:
                    self.postorderTraversal(child)
            self.lst.append(root.val)