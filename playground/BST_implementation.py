from collections import deque
    
class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = left
        self.left = right

class binarySearchTree:
    def __init__(self, l1=[]):
        if len(l1) == 0:
            self.root = Node(0)
            return
        else:
            self.root = Node(l1[0])
            for num in l1:
                self.insert_node_init(self.root, num)
                
    def insert_node_init(self, node, num):
        if node and node.val > num:
            #go left
            if node.left is not None:
                self.insert_node_init(node.left, num)
            else:
                node.left = Node(num)
        elif node and node.val < num:
            #go right
            if node.right is not None:
                self.insert_node_init(node.right, num)
            else:
                node.right = Node(num)
    
    def printInOrder(self, node = None):
        #in order traversal
        if node:
            self.printInOrder(node.left)
            print(node.val, end = " ")
            self.printInOrder(node.right)
    
    def printPreOrder(self, node = None):
        #in order traversal
        if node:
            print(node.val, end = " ")
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)
    
    def printPostOrder(self, node = None):
        #in order traversal
        if node:
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)
            print(node.val, end = " ")

    def printLevelOrder(self):
        q = deque([self.root])
        res = []
        reverse = True
        while q:
            lenq= len(q)
            level = []
            reverse = not reverse
            
            for i in range(lenq):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if reverse:
                res.append(level)
            else:
                res.append(level[::-1])
        print(res)

            
    def printZigZagOrder(self):
        #needs work
        q = deque([self.root])
        res = []
        reverse = True
        while q:
            lenq= len(q)
            level = []
            reverse = not reverse
            
            for i in range(lenq):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if reverse:
                res.append(level)
            else:
                res.append(level[::-1])
        print(res)
        
l1 = [11, 6 , 9, 20, 4, 10, 5, 17, 42, 50, 30]

b1= binarySearchTree(l1)
print("\nprintInOrder")
b1.printInOrder(b1.root)

print("\nprintPreOrder")
b1.printPreOrder(b1.root)

print("\nprintPostOrder")
b1.printPostOrder(b1.root)

print("\nprintLevelOrder")
b1.printLevelOrder()

print("\nprintZigZagOrder")
b1.printZigZagOrder()
