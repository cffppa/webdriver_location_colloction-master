#coding=utf-8
from selenium import webdriver
from time import sleep
import os
import random

file_path = 'file:///'+os.path.abspath('locator.html')
dr = webdriver.Chrome()
dr.get(file_path)

#Task3.1	Select an option by value
dr.find_element_by_css_selector('option[value="4"]').click()
sleep(3)


#Task3.2	Select an option by text
selections = dr.find_elements_by_tag_name('option')
for select in selections:
	if select.get_attribute('text') == 'jack':
		select.click()
sleep(3)

#Task3.3
#Define a method that random select an option and return its text
selections = dr.find_elements_by_tag_name('option')
def random_select():
	option = random.choice(selections)
	option.click()
	text = option.get_attribute('text')
	return text
	
random_select()
print 'choice the %s option' %random_select()
sleep(5)

dr.quit()