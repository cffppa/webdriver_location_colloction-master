#coding=utf-8
from selenium import webdriver
from time import sleep
import os

file_path = 'file:///'+os.path.abspath('locator.html')
dr = webdriver.Chrome()
dr.get(file_path)
sleep(2)

#Task 7
frame = dr.find_element_by_css_selector('iframe.cke_wysiwyg_frame.cke_reset')
dr.switch_to_frame(frame)

textarea = dr.find_element_by_css_selector('body[contenteditable="true"]')
textarea.send_keys('inside,gffshsfghsfghsfghfghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhsfgshgfhsfgh')
sleep(3)

dr.quit()