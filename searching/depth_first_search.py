from Data_Structures.BST import BinarySearchTree, Node


class BstDfs(BinarySearchTree):

    def in_order_traversal(self, node: Node, visit_func):
        if node is not None:
            self.in_order_traversal(node.left, visit_func)
            visit_func(node.data)
            self.in_order_traversal(node.right, visit_func)

    def pre_order_traversal(self, node: Node, visit_func):
        if node is not None:
            visit_func(node.data)
            self.pre_order_traversal(node.left, visit_func)
            self.pre_order_traversal(node.right, visit_func)

    def post_order_traversal(self, node: Node, visit_func):
        if node is not None:
            self.post_order_traversal(node.left, visit_func)
            self.post_order_traversal(node.right, visit_func)
            visit_func(node.data)
