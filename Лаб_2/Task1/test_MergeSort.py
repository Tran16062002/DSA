import unittest
import random
from Лаб_2.Task1.Task1 import mergeSort

class TestMergeSort(unittest.TestCase):
    def test_sort_large_array(self):
        large_array = [random.randint(1,10000) for _ in range(10000)]
        sorted_array = sorted(large_array)
        mergeSort(large_array)
        self.assertEqual(large_array, sorted_array)

if __name__ == '__main__':
    unittest.main()

