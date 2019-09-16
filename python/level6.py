#coding=utf-8
from selenium import webdriver
from time import sleep
import os

file_path = 'file:///'+os.path.abspath('locator.html')
dr = webdriver.Chrome()
dr.get(file_path)
sleep(2)

#Task 6.1  Type something in the outsize textfield
out = dr.find_element_by_name('outsize')
out.send_keys('outside')
sleep(3)

#Task 6.2	Type something in the inside textfield
frame = dr.find_element_by_tag_name('iframe')
dr.switch_to_frame(frame)
inside = dr.find_element_by_name('inside')
inside.send_keys('inside')
sleep(3)

dr.quit()