import os
from selenium import webdriver
import time

filepath='file:///'+os.path.abspath('locator.html')

dr=webdriver.Chrome()
dr.get(filepath)

input='cff test'
#level1
#by_id
ele1=dr.find_element_by_id('name')
ele1.send_keys(input)
assert ele1.get_attribute('value')==input

#by_name
ele2=dr.find_element_by_name('eason')
ele2.send_keys(input)
assert ele2.get_attribute('value')==input

#by_class
#dr.find_element_by_class_name('han').send_keys('cff_by_class')
#dr.find_element_by_xpath('//input[@class="form-control han"]').send_keys('class>by xpath')
ele3=dr.find_element_by_css_selector('input[class="form-control han"]')
ele3.send_keys(input)
assert ele3.get_attribute('value')==input

#by_link
ele4=dr.find_element_by_link_text('easonhan.info')
ele4.click()

#by_css_selector
ele5=dr.find_element_by_css_selector('#for-css')
ele5.send_keys(input)
assert ele5.get_attribute('value')==input
#disable the css_selector input
disabled_js="$('#for-css').attr('disabled',true);"
dr.execute_script(disabled_js)
assert ele5.get_attribute('disabled')=='true'


#by_xpath
ele6=dr.find_element_by_xpath('//input[@id="for-xpath"]')
ele6.send_keys(input)
assert ele6.get_attribute('value')==input

#read_only
ele7=dr.find_element_by_id('readonly')
#方法1，将readonly属性值设置为false
#remove_read_js="$('#readonly').attr('readonly',false)"    
#dr.execute_script(remove_read_js)
#ele.send_keys('hahaha')
#assert ele.get_attribute('value')=='hahaha'
#方法2，直接给输入框赋值
set_value_js="$('#readonly').attr('value','%s')" %(input)
dr.execute_script(set_value_js)
print (ele7.get_attribute('value'))  #这一步获得的值是input变量的值
ele7.send_keys('weiweiwei') #这一步不能实现。文本框还是禁止输入的


#with tag name
ele8=dr.find_element_by_css_selector('input[index="one"]')
ele8.send_keys('cff_test_1')
ele9=dr.find_element_by_css_selector('input[index="two"]')
ele9.send_keys('cff_test_2')
ele10=dr.find_element_by_css_selector('input[index="three"]')
ele10.send_keys('cff_test_3')

assert ele8.get_attribute('value')=='cff_test_1'
assert ele9.get_attribute('value')=='cff_test_2'
assert ele10.get_attribute('value')=='cff_test_3'

#dr.quit()
