'''
Created on Nov 27, 2018

@author: Sharon
'''
# coding = utf-8  
  
from selenium import webdriver   
from selenium.webdriver.common.keys import Keys
import os,time
import unittest
from time import sleep

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        
    
    def tearDown(self):
        self.browser.quit()
        
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")
        
        #check title and header if have the name of To-Do
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        #check input box 
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        
        #Input an errand to do
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        
        sleep(10)
        
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        #sleep(10)
 
        """self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do itme did not appear in table"
        )
        """
        self.check_for_row_in_list_table('Buy peacock feathers')
        self.check_for_row_in_list_table('Use peacock feathers to make a fly')
        
       
        self.fail('Finish the test!')

if __name__ == "__main__":
    unittest.main()
    