import unittest
from sorting.counting_sort import CountingSort


class TestQuickSort(unittest.TestCase):
    
    def test_sort_None_input(self):
        with self.assertRaises(TypeError):
            counting_sort = CountingSort()

    def test_sort_Empty_input(self):
        counting_sort = CountingSort([])
        self.assertEqual(counting_sort.sort(), [])

    def test_sort_One_element(self):
        counting_sort = CountingSort([4])
        self.assertEqual(counting_sort.sort(), [4])

    def test_sort_Two_or_more_elements(self):
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        counting_sort = CountingSort(data)
        self.assertEqual(counting_sort.sort(), sorted(data))

