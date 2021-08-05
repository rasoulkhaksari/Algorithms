import unittest
from sorting.merge_sort import MergeSort


class TestMergeSort(unittest.TestCase):
    
    def test_sort_None_input(self):
        with self.assertRaises(TypeError):
            merge_sort = MergeSort()

    def test_sort_Empty_input(self):
        merge_sort = MergeSort([])
        self.assertEqual(merge_sort.sort(), [])

    def test_sort_One_element(self):
        merge_sort = MergeSort([4])
        self.assertEqual(merge_sort.sort(), [4])

    def test_sort_Two_or_more_elements(self):
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        merge_sort = MergeSort(data)
        self.assertEqual(merge_sort.sort(), sorted(data))

