#coding=utf-8
from selenium import webdriver
import os
import random
import time

file_path='file:///'+os.path.abspath('locator.html')

dr=webdriver.Chrome()
dr.get(file_path)
'''
#checkboxes
#task 2.1 选择所有checkbox-----------------------------------------
eles=dr.find_elements_by_css_selector('[type="checkbox"]')

for ele in eles:
	ele.click()

#task2.2 选择前两个checkbox-----------------------------------------
eles[0].click()
eles[1].click()
#或者
for i in range(0,2):
	eles[i].click()

#task 2.3 选择最后两个checkbox-----------------------------------------
for i in range(2,4):
	eles[i].click()

#task 2.4 随机选择一个checkbox-----------------------------------------
eles[random.randint(0,3)].click()
#或者
ele=random.choice(eles)
ele.click()

#task 2.5 随机选择两个checkbox-----------------------------------------
eles=dr.find_elements_by_css_selector('[type="checkbox"]')
for i in range(0,2):
	ele=random.choice(eles)
	ele.click()
	eles.remove(ele)
	

#task 2.6 toggle select：如果已勾选，就不勾选，如果没勾选就勾选
#方法1.用.is_selected()函数判断
eles=dr.find_elements_by_css_selector('[type="checkbox"]')
eles[0].click()
eles[3].click()
for ele in eles:
	if ele.is_selected():
		ele.click()
	else:
		ele.click()
#方法2.用jquery实现
js='$(\'[type="checkbox"]\').each(function(){ if ($(this).prop(\'checked\')){$(this).prop(\'checked\',false)}else{$(this).prop(\'checked\',true)}});'
dr.execute_script(js)

#task2.7 Define a method which accept 1 parameters(count). This method will random select checkboxes with quantity of count.
eles=dr.find_elements_by_css_selector('[type="checkbox"]')
def random_select(count):
	
	if count==0:
		print ('none checkbox select')
	else:
		for i in range(0,count):
			ele=random.choice(eles)
			ele.click()
			eles.remove(ele)

select_num=random.randint(0,4)    #0-4随机取数，比如取2就是任选2个元素。取3就是任选3个元素
print (select_num)
random_select(select_num)


#task2.8 select radio by value
ele1=dr.find_element_by_xpath("//input[@name=\'radio_name\'and @value=\'first\']")
ele1.click()
assert ele1.get_attribute('value')=='first'

#task 2.9 random select one radio
eles=dr.find_elements_by_name('radio_name')
ele=random.choice(eles)
ele.click()
'''

#task 2.10
'''
Define a method which accept 2 parameters(type, count).
If the type is checkbox, random select checkboxes with quantity count.
If the type is radio, random select one radio.
'''
checkboxes=dr.find_elements_by_css_selector("[type='checkbox']")
radios=dr.find_elements_by_name('radio_name')

def random_select(type,count):
	if type=='checkbox':	
		if count>0 and count<=len(checkboxes):
			for i in range(0,count):
				checkbox=random.choice(checkboxes)
				checkbox.click()
				checkboxes.remove(checkbox)
		else:
			print ('"count" is out of range')
	else :
		radio=random.choice(radios)
		radio.click()

 

random_select('radio',2)
random_select('checkbox',0)
random_select('checkbox',5)
random_select('checkbox',3)




