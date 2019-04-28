from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def send_input_to_list_item(self, inputbox, item_text):
        inputbox.send_keys(item_text)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

    def test_can_start_a_list_and_retrieve_later(self):
        # Open Homepage
        self.browser.get(self.live_server_url)

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
        self.send_input_to_list_item(inputbox,'Read Chapter 6 of Two Scoops')

        self.check_for_row_in_list_table( "1: Read Chapter 6 of Two Scoops")

        # Add a second entry "Read Chapter 7 of Two Scoops"
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.send_input_to_list_item(inputbox,'Read Chapter 7 of Two Scoops')
        
        # Check page update and lists the entries now as
        # 1. Read Chapter 6 of Two Scoops
        # 2. Read Chapter 7 of Two Scoops
        self.check_for_row_in_list_table("1: Read Chapter 6 of Two Scoops")
        self.check_for_row_in_list_table("2: Read Chapter 7 of Two Scoops")


        # Check To Do List with Test Name Edith in URL
        self.fail("Finish The Test")


