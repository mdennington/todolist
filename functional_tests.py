from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_later(self):
        # Open Homepage
        self.browser.get('http://localhost:8000')

        # Check title is "To Do"
        self.assertIn('To Do', self.browser.title)
        self.fail('Finish The Test!')

        # Enter a to do item

        # Type "Read Chapter 6 of Two Scoops"

        # Check page updates and lists the entry as
        # 1. Read Chapter 6 of Two Scoops

        # Add a second entry "Read Chapter 7 of Two Scoops"

        # Check page update and lists the entries now as
        # 1. Read Chapter 6 of Two Scoops
        # 2. Read Chapter 7 of Two Scoops

        # Check To Do List with Test Name Edith in URL


if __name__ == '__main__':
    unittest.main(warnings='ignore')

