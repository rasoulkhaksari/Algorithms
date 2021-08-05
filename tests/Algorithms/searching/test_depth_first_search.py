import unittest
from searching.depth_first_search import BstDfs
from data_structure.BST import Node
from utils.results import Results

class TestDfs(unittest.TestCase):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.results = Results()

    def test_in_order_traversal(self):
        """Test Binary Search Tree Depth First Search: (in order traversal)"""
        bst = BstDfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)

        bst.in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(self.results.get_all(), [1, 2, 3, 5, 8])
        self.results.clear_results()

    def test_pre_order_traversal(self):
        """Test Binary Search Tree Depth First Search: (pre order traversal)"""
        bst = BstDfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)

        bst.pre_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(self.results.get_all(), [5, 2, 1, 3, 8])
        self.results.clear_results()

    def test_post_order_traversal(self):
        """Test Binary Search Tree Depth First Search: (post order traversal)"""
        bst = BstDfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)

        bst.post_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(self.results.get_all(), [1, 3, 2, 8, 5])
        self.results.clear_results()

