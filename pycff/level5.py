from selenium import webdriver
import time,os

file_path="file:///"+os.path.abspath('locator.html')
dr=webdriver.Chrome()
dr.get(file_path)



text='easonhan.info'

#task5.1 在新开百度窗口输入easonhan------------------------------------
ele=dr.find_element_by_link_text('Baidu')
ele.click()
print (dr.title)
print (dr.current_url)
#获得当前窗口句柄
current_handle=dr.current_window_handle
print (current_handle)
#获得所有窗口句柄
all_handles=dr.window_handles
print (all_handles)

for i in all_handles:
	if i!=current_handle:
		dr.switch_to.window(i)


ele1=dr.find_element_by_id('kw')
ele1.send_keys(text)


#task5.2 在当前窗口输入easonhan-------------------------------------------
ele=dr.find_element_by_link_text('Baidu')
link=ele.get_attribute('href')
print(link)

dr.get(link)
ele2=dr.find_element_by_id('kw')
ele2.send_keys(text)

dr.quit()