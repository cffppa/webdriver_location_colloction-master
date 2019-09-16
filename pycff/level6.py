from selenium import webdriver
import time,os

file_path="file:///"+os.path.abspath('locator.html')
dr=webdriver.Chrome()

dr.get(file_path)
time.sleep(3)

#task6.1 type someshing in the outsize textfield
ele1=dr.find_element_by_name('outsize')
ele1.send_keys('kkkkkkkkkkk')




#task 6.2 type something in the inside textfield
iframe=dr.find_element_by_tag_name('iframe')
dr.switch_to_frame(iframe)
ele2=dr.find_element_by_name('inside')
ele2.send_keys('jhhhhhh')


dr.quit()
