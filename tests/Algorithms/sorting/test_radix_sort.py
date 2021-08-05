import unittest
from sorting.radix_sort import RadixSort


class TestMergeSort(unittest.TestCase):
    
    def test_sort_None_input(self):
        with self.assertRaises(TypeError):
            radix_sort = RadixSort()

    def test_sort_Empty_input(self):
        radix_sort = RadixSort([])
        self.assertEqual(radix_sort.sort(), [])

    def test_sort_One_element(self):
        radix_sort = RadixSort([4])
        self.assertEqual(radix_sort.sort(), [4])

    def test_sort_Two_or_more_elements(self):
        data = [5, 1, 7, 2, 6, 3, 5, 7, 1]
        radix_sort = RadixSort(data)
        self.assertEqual(radix_sort.sort(), sorted(data))

