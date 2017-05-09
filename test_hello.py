import unittest
#from hello import somefunction

class HelloTestCase(unittest.TestCase):
    #Tests for `hello.py`

    def test_something(self):
        #What does this test?
        self.assertTrue(somefunction(sometestcase))

if __name__ == '__main__':
    unittest.main()
