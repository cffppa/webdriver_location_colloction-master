from selenium import webdriver
import os
import time
import random

file_path="file:///"+os.path.abspath('locator.html')

dr=webdriver.Chrome()
dr.get(file_path)

'''
#level3
#task3.1 by value
ele=dr.find_element_by_css_selector("option[value='3']")
ele.click()
print (ele.text)
assert ele.text=='jack'


#task3.2 by_text
eles=dr.find_elements_by_tag_name('option')
for ele in eles:
	if ele.get_attribute('text')=='jack':
		ele.click()
time.sleep(3)
'''

#task3.3 Define a method that random select an option and return its text
eles=dr.find_elements_by_tag_name('option')

def random_choice():
	ele=random.choice(eles)
	ele.click()
	text=ele.get_attribute('text')
	print (text)
	return (text)

random_choice()



