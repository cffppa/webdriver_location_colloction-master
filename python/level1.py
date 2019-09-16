#coding=utf-8

from selenium import webdriver
from time import sleep
import os
import re #用正则表达式库

file_path = 'file:///'+os.path.abspath('locator.html')
dr = webdriver.Chrome()
dr.get(file_path)

input_word = 'tttexfagadg'

#with id
id_element = dr.find_element_by_id('name')
id_element.send_keys(input_word)
assert id_element.get_attribute('value') == input_word
sleep(3)

#with name
name_element = dr.find_element_by_name('eason')
name_element.send_keys(input_word)
assert name_element.get_attribute('value') == input_word
sleep(3)

#with class
class_element = dr.find_element_by_class_name('han')
class_element.send_keys(input_word)
assert class_element.get_attribute('value') == input_word
sleep(3)


#上面的with class用xpath
xpath_element = dr.find_element_by_xpath('//input[@class="form-control han"]')
xpath_element.send_keys('xpath')
assert xpath_element.get_attribute('value') == (input_word+'xpath')
sleep(2)

#上面的with class用css selector
css_selector_1 = dr.find_element_by_css_selector('input[class="form-control han"]')
css_selector_1.send_keys('css')
assert css_selector_1.get_attribute('value') == (input_word+'xpath'+'css')
sleep(2)


#with link text
link_element = dr.find_element_by_link_text('easonhan.info')
link_element.click()
assert link_element.text == 'easonhan.info'
sleep(3)


#with css selector
css_selector_2 = dr.find_element_by_css_selector('#for-css')
css_selector_2.send_keys(input_word)
assert css_selector_2.get_attribute('value') == input_word

#with xpath
xpath_element_2 = dr.find_element_by_xpath('//input[@id="for-xpath"]')
xpath_element_2.send_keys(input_word)
assert xpath_element_2.get_attribute('value') == input_word


#正则表达式定位：match id ~= ^for inputs and input something  #找到for开头的input
inputs = dr.find_elements_by_tag_name('input')
#disable掉id=for-css的输入框.禁止输入
disable_js = '$("#for-css").attr("disabled","disabled");'
dr.execute_script(disable_js)
leading_str = 'Leading with for'
for ip in inputs:
	if re.search('^for.*',ip.get_attribute('id')):
		if ip.get_attribute('type') == 'text' and ip.is_enabled(): #如果是可输入文本框。input标签的默认type是text
			ip.clear()
			ip.send_keys(leading_str)
assert dr.find_element_by_id('for-xpath').get_attribute('value') == leading_str
print dr.find_element_by_id('for-css').get_attribute('disabled') 
assert dr.find_element_by_id('for-css').get_attribute('disabled') == 'true'
sleep(3)

#with readonly
#禁止的输入框实现输入。（推荐使用第二种不改变前端的方法）
#方法1 通过删掉readonly属性，来实现输入
remove_readonly_js = "$('#readonly').removeAttr('readonly')"
dr.execute_script(remove_readonly_js)   
readonly_element = dr.find_element_by_id('readonly')
readonly_element.send_keys(input_word)
assert readonly_element.get_attribute('value') == input_word
sleep(3)

#方法2：直接赋值
set_value_to_readonly_js = "$('#readonly').attr('value','%s')"  %(input_word)
dr.execute_script(set_value_to_readonly_js)
readonly_element = dr.find_element_by_id('readonly')
readonly_element.send_keys(input_word)
assert readonly_element.get_attribute('value') == input_word
sleep(5)


#with tag name
#示范用js实现
#定位到index=one的元素
locate_index_one_js = "return $('input[index=\"one\"]');"   #把js获取到的值返回，作为一个dom元素传到webdriver
the_list = dr.execute_script(locate_index_one_js)   #jequry return的是个list.index=one的只有一个，所以list只有一个元素。
#print the_list   
#print the_list[0]
#print the_list[0].__class__
the_list[0].send_keys(input_word)
assert dr.find_element_by_css_selector("input[index='one']").get_attribute('value') == input_word
sleep(3)


#判断index=four的元素是否存在
#方法1：用js
exists_js = 'return $("input[index=%s]").length' %("four")
res = dr.execute_script(exists_js)
if res>0:
	print "element index='four' exist"
else:
	print "element index='four' not exist"
#方法同上，不过是自定义了一个exists函数
#自定义一个判断元素是否存在的函数
def exists(dr,css_locator):
	js = 'return $(\'%s\').length' %(css_locator)
	print js
	if dr.execute_script(js)>0:
		return True
	else:
		return False

if(exists(dr,'input[index="five"]')):
	print 'ok'
else:
	print 'element index="five" not exist'

#方法2：用try except

try :
	if dr.find_element_by_css_selector('input[index="six"]'):
		print 'element exist'
except:
	print 'element index="six" not exist.'



#截图:用save_screenshot
picture_js = '$(\'<div class=\"alert alert-info\">出大事了</div>\').insertAfter(".jumbotron");'
dr.execute_script(picture_js)
dr.save_screenshot('./screenshot.png')

dr.quit()