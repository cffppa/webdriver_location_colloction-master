#coding=utf-8
from selenium import webdriver
from time import sleep
import os

file_path = 'file:///'+os.path.abspath('locator.html')
dr = webdriver.Chrome()
dr.get(file_path)

#Simple alert
buttons = dr.find_elements_by_class_name('btn')
for button in buttons:
	if button.get_attribute('text')=='Alert Button':
		button.click()
		break
sleep(3)

try:
	alert = dr.switch_to_alert()
	print alert.text
	alert.accept()
except:
	print 'click the alert button!'


#simple confrim
confrim_button = dr.find_element_by_link_text('Confirm Button')
confrim_button.click()
sleep(3)

try:
	alert = dr.switch_to_alert()
	print alert.text
	#alert.accept()  接受警告信息
	alert.dismiss()  #取消对话框
	sleep(3)
except:
	print 'No alert!'


#prompt button
Prompt_Button = dr.find_element_by_link_text('Prompt Button')
Prompt_Button.click()
sleep(3)

try:
	alert = dr.switch_to_alert()
	sleep(3)
	alert.send_keys('hahahahah')
	sleep(3)
	print alert.text
	alert.accept()
	sleep(3)
except:
	print 'No alert'



dr.quit()