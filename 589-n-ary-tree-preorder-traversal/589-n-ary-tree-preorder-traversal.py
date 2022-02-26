"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.lst = []
        self.preorderTraversal(root)
        return self.lst
        
    
    def preorderTraversal(self, root: 'Node') -> List[int]:
        if root:
            self.lst.append(root.val)
            for child in root.children:
                if child:
                    self.preorderTraversal(child)