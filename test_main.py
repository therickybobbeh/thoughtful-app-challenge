import unittest
from unittest.mock import patch
from main import sort, main


class TestSort(unittest.TestCase):

    def test_standard_package(self):
        """Test for STANDARD case: large volume, light mass"""
        self.assertEqual(sort(100, 100, 100, 10), "STANDARD")

    def test_special_package_large_heavy(self):
        """Test for SPECIAL case: large volume, heavy mass"""
        self.assertEqual(sort(200, 200, 200, 25), "SPECIAL")

    def test_special_package_small_heavy(self):
        """Test for SPECIAL case: small volume, heavy mass"""
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")

    def test_rejected_package(self):
        """Test for REJECTED case: small volume, light mass"""
        self.assertEqual(sort(50, 50, 50, 10), "REJECTED")

    @patch('builtins.input', side_effect=["100", "100", "100", "10"])
    @patch('builtins.print')
    def test_main_standard(self, mock_print, mock_input):
        """Test main function for STANDARD case."""
        main()
        mock_print.assert_any_call("The object is classified as: STANDARD")

    @patch('builtins.input', side_effect=["200", "200", "200", "25"])
    @patch('builtins.print')
    def test_main_special(self, mock_print, mock_input):
        """Test main function for SPECIAL case."""
        main()
        mock_print.assert_any_call("The object is classified as: SPECIAL")

    @patch('builtins.input', side_effect=["50", "50", "50", "10"])
    @patch('builtins.print')
    def test_main_rejected(self, mock_print, mock_input):
        """Test main function for REJECTED case."""
        main()
        mock_print.assert_any_call("The object is classified as: REJECTED")


if __name__ == '__main__':
    unittest.main()
