from selenium import webdriver
import time,os

file_path="file:///"+os.path.abspath('locator.html')
dr=webdriver.Chrome()
dr.get(file_path)

text='/********^$($($&($&*(*********/'
'''
#方法1：常规元素定位
frame=dr.find_element_by_css_selector('iframe.cke_wysiwyg_frame.cke_reset')
dr.switch_to_frame(frame)

ele=dr.find_element_by_css_selector('body[contenteditable="true"]')
ele.send_keys(text)
'''
#方法2：用js
set_js="document.getElementsByTagName('iframe')[1].contentWindow.document.body.innerHTML='%s'" %text
dr.execute_script(set_js)






time.sleep(5)