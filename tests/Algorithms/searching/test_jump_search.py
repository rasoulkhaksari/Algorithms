from searching.jump_search import JumpSearch
import unittest

class TestJumpSearch(unittest.TestCase):

    def test_find(self):
        data = [5,1,4,9,2,5]
        js = JumpSearch(data)
        self.assertEqual(js.find(4), 2)
        self.assertEqual(js.find(10), -1)
