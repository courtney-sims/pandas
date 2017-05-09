import unittest
from randomfact import paragraphs

class RandomFactTestCase(unittest.TestCase):
    #Tests for `randomfact.py`

    def test_facts_exist(self):
        #Are we getting any facts from the facts file?
        self.assertIsNotNone(paragraphs('test_pandafacts.txt'), msg="I don't know if facts exist :(")

    def test_4_paragraphs(self):
        #Is the facts file being properly split into facts by paragraph?
        self.assertEqual(len(paragraphs('test_pandafacts.txt')),4, msg="I don't know if facts are counted :(")

if __name__ == '__main__':
    unittest.main()
