Identify if both vals are in left or right subtree from current node.
​
As this is Binary Tree:
1. Elminate left half or right half if both values are smaller or greater than curr_node
2. if root.val is between both values, we have found our common ancestor
​
Properties of BST:
1. All values on left half < root values for each subtree
2. All values on right half  > root values for each subtree
3. BST gets sorted in inOrder traversal
​
Types of Tree Traversals:
1. PreOrder traversal : (root val processed first)
2. PostOrder Traversal : (root val processed last)
3. InOrder traversal : (left root right) (BST gets sorted)
4. Level Order Traversal : use deque (BFS)
5. ZigZag level order traversal : alternately use stack and q to retrive elements to get ZigZag or use deque to alternatly popleft/append and pop/appendleft
6. Vertical order traversal : DFS, pass row+1 and col+-1 right/left and store (row, val) in map
7. Reverse Level Order Traversal :