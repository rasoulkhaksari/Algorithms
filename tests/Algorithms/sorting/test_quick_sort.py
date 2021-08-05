import unittest
from sorting.quick_sort import QuickSort


class TestQuickSort(unittest.TestCase):
    
    def test_sort_None_input(self):
        with self.assertRaises(TypeError):
            quick_sort = QuickSort()

    def test_sort_Empty_input(self):
        quick_sort = QuickSort([])
        self.assertEqual(quick_sort.sort(), [])

    def test_sort_One_element(self):
        quick_sort = QuickSort([4])
        self.assertEqual(quick_sort.sort(), [4])

    def test_sort_Two_or_more_elements(self):
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        quick_sort = QuickSort(data)
        self.assertEqual(quick_sort.sort(), sorted(data))

    def test_sort_Two_or_more_elements_v2(self):
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        quick_sort = QuickSort(data)
        self.assertEqual(quick_sort.sort_v2(0,len(data)-1), sorted(data))
