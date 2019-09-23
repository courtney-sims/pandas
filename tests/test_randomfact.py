"""
This module provides unit tests for the randomfact module.
"""
import unittest

from randomfact import paragraphs

class RandomFactTestCase(unittest.TestCase):
    """
    This class tests the code in randomfact.py.
    """
    def setUp(self):
        self.panda_facts_file = 'tests/test_data/test_panda_facts.txt'
    def test_facts_exist(self):
        """
        This method tests paragraphs().
        It ensures a test file can be parsed to return information.
        """
        test_facts = paragraphs(self.panda_facts_file)
        self.assertIsNotNone(test_facts, msg="I don't know if facts exist :(")

    def test_4_paragraphs(self):
        """
        This method tests paragraphs().
        It ensures a test file can be split into the expected number of paragraphs.
        """
        expected_length = 4
        actual_length = len(paragraphs(self.panda_facts_file))
        self.assertEqual(actual_length, expected_length, msg="I don't know if facts are counted :(")

if __name__ == '__main__':
    unittest.main()
