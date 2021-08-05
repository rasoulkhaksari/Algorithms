import unittest
from sorting.selection_sort import SelectionSort


class TestSelectionSort(unittest.TestCase):
    def test_sort_None_input(self):
        with self.assertRaises(TypeError):
            selection_sort = SelectionSort()

    def test_sort_Empty_input(self):
        selection_sort = SelectionSort([])
        self.assertEqual(selection_sort.sort(), [])

    def test_sort_One_element(self):
        selection_sort = SelectionSort([4])
        self.assertEqual(selection_sort.sort(), [4])

    def test_sort_Two_or_more_elements(self):
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        selection_sort = SelectionSort(data)
        self.assertEqual(selection_sort.sort(), sorted(data))
