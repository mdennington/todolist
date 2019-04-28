from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To Do', header_text)

        # Enter a to do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Type "Read Chapter 6 of Two Scoops"
        inputbox.send_keys('Read Chapter 6 of Two Scoops')

        # Check page updates and lists the entry as
        # 1. Read Chapter 6 of Two Scoops
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Read Chapter 6 of Two Scoops', [row.text for row in rows])

        # Add a second entry "Read Chapter 7 of Two Scoops"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Read Chapter 7 of Two Scoops')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        # Check page update and lists the entries now as
        # 1. Read Chapter 6 of Two Scoops
        # 2. Read Chapter 7 of Two Scoops
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            "1: Read Chapter 6 of Two Scoops", 
            [row.text for row in rows]
        )
        self.assertIn(
            "2: Read Chapter 7 of Two Scoops", 
            [row.text for row in rows]
        )

        # Check To Do List with Test Name Edith in URL
        self.fail("Finish The Test")

if __name__ == '__main__':
    unittest.main(warnings='ignore')

