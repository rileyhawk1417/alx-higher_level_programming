#!/usr/bin/python3
"""Unit test for max_integer function"""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInt(unittest.TestCase):
    """Define unittests for max_integer"""

    def test_ordered_list(self):
        """Test a ordered list of integers"""
        ordered = [2, 4, 6, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered_list(self):
        """Test a unordered list of integers"""
        unordered = [4, 8, 2, 6]
        self.assertEqual(max_integer(unordered), 8)

    def test_max_at_start(self):
        """Test a list with a start max value"""
        max_at_start = [8, 6, 4, 2]
        self.assertEqual(max_integer(max_at_start), 8)

    def test_an_empty_list(self):
        """Test an empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_el(self):
        """Test a list with one element"""
        one_el = [4]
        self.assertEqual(max_integer(one_el), 4)

    def test_floats(self):
        """Test a list with float numbers"""
        float_list = [2.50, 4.35, 6.75, 8.90]
        self.assertEqual(max_integer(float_list), 8.90)

    def test_float_ints(self):
        """Test a list of integers & floats"""
        float_int = [2, 3.45, 4, 5.65, 6, 7.20, 8]
        self.assertEqual(max_integer(float_int), 8)

    def test_string(self):
        """Test a string value"""
        string_input = "Spidey"
        self.assertEqual(max_integer(string_input), "y")

    def test_string_list(self):
        """Test a list of strings"""
        string_list = ["I", "am", "Spiderman"]
        self.assertEqual(max_integer(string_list), "am")

    def test_empty_string(self):
        """Test a empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
