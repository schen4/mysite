'''
Created on Nov 27, 2018

@author: Sharon
'''
# coding = utf-8  
  
from selenium import webdriver   
import time
  
browser = webdriver.Chrome()  
browser.maximize_window()  
url = 'http://localhost:8000'  
browser.get(url)  
time.sleep(2)
assert 'Django' in browser.title
browser.close()