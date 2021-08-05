from searching.binary_search import BinarySearch
import unittest

class TestBinarySearch(unittest.TestCase):

    def test_find(self):
        data = [5,1,4,9,2,5]
        bs = BinarySearch(data)
        self.assertEqual(bs.find(4), 2)
        self.assertEqual(bs.find(10), -1)
