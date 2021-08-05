import unittest
from utils.results import Results
from data_structure.BST import Node
from searching.breath_first_search import BstBfs

class TestBfs(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.results = Results()

    def test_bfs(self):
        """Test: Binary Search Tree Breath First Search"""
        bst = BstBfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        bst.bfs(self.results.add_result)
        self.assertEqual(self.results.get_all(), [5, 2, 8, 1, 3])




