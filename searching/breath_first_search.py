from Data_Structures.BST import BinarySearchTree, Node
from collections import deque


class BstBfs(BinarySearchTree):

    def bfs(self, visit_func):
        if self.root is None:
            raise TypeError("BST is None")
        queue = deque()
        queue.append(self.root)
        while queue:
            node: Node = queue.popleft()
            visit_func(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
