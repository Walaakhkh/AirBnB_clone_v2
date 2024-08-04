#!/usr/bin/python3
import unittest
from console import Console

class TestConsole(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.console = Console()

    def test_some_feature(self):
        """Test some feature of the console"""
        self.assertTrue(self.console.some_function())

if __name__ == '__main__':
    unittest.main()
