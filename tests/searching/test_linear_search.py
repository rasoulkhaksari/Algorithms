from searching.linear_search import LinearSearch
import unittest

class TestLinearSearch(unittest.TestCase):

    def test_find(self):
        data = [1,2,3,4,5,6]
        ls = LinearSearch(data)
        self.assertEqual(ls.find(5), 4)
        self.assertEqual(ls.find(10), -1)


# if __name__ == '__main__':
#     unittest.main()

