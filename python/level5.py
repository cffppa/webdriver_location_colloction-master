#coding=utf-8
from selenium import webdriver
from time import sleep
import os

file_path = 'file:///'+os.path.abspath('locator.html')
dr = webdriver.Chrome()
dr.get(file_path)
sleep(2)

'''
#--------------------------Task 5.1-----------------------------------
#当前句柄
current_handle = dr.current_window_handle
print current_handle
print dr.title

link = dr.find_element_by_link_text('Baidu')
link.click()
sleep(5)

#定位到新开窗口的句柄
all_handles = dr.window_handles
for handle in all_handles:
	if handle != current_handle:
		locate_handle = handle

new_handle = dr.switch_to_window(locate_handle)
sleep(3)
print dr.title

dr.find_element_by_id('kw1').send_keys('easonhan.info')
sleep(3)
'''

#------------------------Task 5.2-----------------------------
link = dr.find_element_by_link_text('Baidu')
href = link.get_attribute('href')
assert href == 'http://www.baidu.com/'

dr.get(href)
print dr.title
assert dr.title == u'百度一下，你就知道'
dr.find_element_by_id('kw1').send_keys('easonhan.info')
sleep(3)

dr.quit()

