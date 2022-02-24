print("Hello World!uhnngjhgng")

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
            print(node.val)
            self.printInOrder(node.right)
    
    def printPreOrder(self, node = None):
        #in order traversal
        if node:
            print(node.val)
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)
    
l1 = [11, 6 , 9, 20, 4, 10, 5, 17, 42, 50, 30]

b1= binarySearchTree(l1)
b1.printInOrder(b1.root)
print("--"*12)
b1.printPreOrder(b1.root)
        
    
