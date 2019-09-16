from selenium import webdriver
import os
import time

file_path="file:///"+os.path.abspath('locator.html')
dr=webdriver.Chrome()
dr.get(file_path)

#level4  alert
#ele=dr.find_element_by_css_selector('a[class="btn btn-lg btn-default"]')
ele1=dr.find_element_by_link_text('Alert Button')
ele1.click()
time.sleep(4)

try:
	alert=dr.switch_to.alert
	print (alert.text)
	alert.accept()
except:
	print ('no alert exist!')

#confirm
ele2=dr.find_element_by_link_text('Confirm Button')
ele2.click()
time.sleep(3)

try:
	alert=dr.switch_to.alert
	print(alert.text)
	alert.dismiss()
except:
	print ('no alert')
time.sleep(3)

#prompt
ele3=dr.find_element_by_link_text('Prompt Button')
ele3.click()
time.sleep(5)

try:
	alert=dr.switch_to.alert
	alert.sendKeys('hhhhhhhh')  #这一步没通过？？
	print(alert.text)

except:
	print ('no alert')

dr.quit()