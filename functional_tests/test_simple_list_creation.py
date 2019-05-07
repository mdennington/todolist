from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def send_input_to_list_item(self, inputbox, item_text):
        inputbox.send_keys(item_text)
        inputbox.send_keys(Keys.ENTER)

    def test_can_start_a_list_for_one_user(self):
        # Open Homepage
        self.browser.get(self.live_server_url)

        # Check title is "To Do"
        self.assertIn('To Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To Do', header_text)

        # Enter a to do item
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Type "Read Chapter 6 of Two Scoops"
        self.send_input_to_list_item(inputbox,'Read Chapter 6 of Two Scoops')

        self.wait_for_row_in_list_table( "1: Read Chapter 6 of Two Scoops")

        # Add a second entry "Read Chapter 7 of Two Scoops"
        inputbox = self.get_item_input_box()
        self.send_input_to_list_item(inputbox,'Read Chapter 7 of Two Scoops')
        
        # Check page update and lists the entries now as
        # 1. Read Chapter 6 of Two Scoops
        # 2. Read Chapter 7 of Two Scoops
        self.wait_for_row_in_list_table("1: Read Chapter 6 of Two Scoops")
        self.wait_for_row_in_list_table("2: Read Chapter 7 of Two Scoops")


    def test_multiple_users_can_start_lists_at_different_URLS(self):
        # Edith Starts a New List
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Read Chapter 2 of Two Scoops")
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table("1: Read Chapter 2 of Two Scoops")

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        self.browser.quit()

        # Francis starts a New List
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Read Chapter 2 of Two Scoops', page_text)
        
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Script automated deployment')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Script automated deployment")

        # Francis gets his own URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Read Chapter 2 of Two Scoops', page_text)
    

