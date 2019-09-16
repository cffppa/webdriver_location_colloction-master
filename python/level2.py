#coding=utf-8
from selenium import webdriver
from time import sleep
import os
import random

file_path = 'file:///'+os.path.abspath('locator.html')
dr = webdriver.Chrome()
dr.get(file_path)

'''
#task 2.1 Select all the checkboxes
checkboxes = dr.find_elements_by_css_selector('input[type="checkbox"]')
for checkbox in checkboxes:
	checkbox.click()
sleep(5)


#task 2.2 select first two checkboxes
checkboxes = dr.find_elements_by_css_selector('input[type="checkbox"]')
for i in range(0,2):
	checkboxes[i].click()
sleep(3)


#Task2.3 Select last two checkboxes
checkboxes = dr.find_elements_by_css_selector('input[type="checkbox"]')
for i in range(2,4):
	checkboxes[i].click()
sleep(3)


#Task2.4	Random select one checkbox
checkboxes =  dr.find_elements_by_css_selector('input[type="checkbox"]')
checkbox = random.choice(checkboxes)
checkbox.click()
sleep(5)

#Task2.5  Random select two checkbox
checkboxes =  dr.find_elements_by_css_selector('input[type="checkbox"]')
for i in range(0,2):
	checkbox = random.choice(checkboxes)
	checkbox.click()
	checkboxes.remove(checkbox)
sleep(5)

#Task2.6	Toggle select checkbox. if the checkbox is selected, unselect it, else select it.







#Task2.7 Level Up!
#Define a method which accept 1 parameters(count). This method will random select checkboxes with quantity of count.
checkboxes = dr.find_elements_by_css_selector('input[type="checkbox"]')
def random_select(count):
	if count>len(checkboxes):
		print "There are only %d checkboxes,the count you given more than that." %len(checkboxes)
	else:
		for i in range(0,count):
			checkbox = random.choice(checkboxes)
			checkbox.click()
			checkboxes.remove(checkbox)
		sleep(3)
random_select(3)
sleep(5)


#Task2.8  Select radio by value.
third = dr.find_element_by_css_selector('input[value="third"]')
third.click()
sleep(3)

#Task2.9	Random select one radio
radios = dr.find_elements_by_name('radio_name')
random.choice(radios).click()
sleep(3)
'''

#Task2.10 Level Up!
#Define a method which accept 2 parameters(type, count).
#If the type is checkbox, random select checkboxes with quantity count.
#If the type is radio, random select one radio.
checkboxes = dr.find_elements_by_css_selector('input[type="checkbox"]')
radios = dr.find_elements_by_name('radio_name')
def random_select_2(type_2,count):
	if type_2==checkboxes and count>len(checkboxes):
		print "There are only %d checkboxes,the count you given more than that." %len(checkboxes)
	elif type_2==radios and count>1:
		print "You could choice the only radio."
	else:
		for i in range(0,count):
			a = random.choice(type_2)
			a.click()
			type_2.remove(a)
			sleep(3)

random_select_2(checkboxes,7)
random_select_2(checkboxes,3)
random_select_2(radios,2)
random_select_2(radios,1)








dr.quit()
