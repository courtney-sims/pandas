"""Test to ensure that Flask will run in the browser."""

import unittest

from selenium import webdriver

class TestFlaskInBrowser(unittest.TestCase):
    """Class for Flask tests in the browser."""
    def test_home_page_load(self):
        """Assert that 'Flask' will show in the tab title of the browser on the home page."""
        browser = webdriver.Firefox()
        browser.get('http://localhost:5000')
        self.assertTrue('Flask' in browser.title)
