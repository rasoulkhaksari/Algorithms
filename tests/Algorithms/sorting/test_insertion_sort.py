import unittest
from sorting.insertion_sort import InsertionSort


class TestInsertionSort(unittest.TestCase):
    def test_sort_None_input(self):
        with self.assertRaises(TypeError):
            insertion_sort = InsertionSort()

    def test_sort_Empty_input(self):
        insertion_sort = InsertionSort([])
        self.assertEqual(insertion_sort.sort(), [])

    def test_sort_One_element(self):
        insertion_sort = InsertionSort([4])
        self.assertEqual(insertion_sort.sort(), [4])

    def test_sort_Two_or_more_elements(self):
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        insertion_sort = InsertionSort(data)
        self.assertEqual(insertion_sort.sort(), sorted(data))
