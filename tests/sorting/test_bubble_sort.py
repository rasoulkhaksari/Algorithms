import unittest
from sorting.bubble_sort import BubbleSort


class TestQuickSort(unittest.TestCase):
    
    def test_sort_None_input(self):
        with self.assertRaises(TypeError):
            bubble_sort = BubbleSort()

    def test_sort_Empty_input(self):
        bubble_sort = BubbleSort([])
        self.assertEqual(bubble_sort.sort(), [])

    def test_sort_One_element(self):
        bubble_sort = BubbleSort([4])
        self.assertEqual(bubble_sort.sort(), [4])

    def test_sort_Two_or_more_elements(self):
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        bubble_sort = BubbleSort(data)
        self.assertEqual(bubble_sort.sort(), sorted(data))

