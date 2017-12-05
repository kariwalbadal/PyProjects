from selenium import webdriver
import sys
from selenium.webdriver.common.keys import Keys
import time
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()

driver  = webdriver.Chrome()
try:
	driver.get('http://192.168.1.1')
except Exception, e:
	print "Check router connection or router IP"
	sys.exit()

time.sleep(1)
d = driver.find_element_by_class_name('input-medium')
d.send_keys('admin')
d = driver.find_element_by_class_name('btn-link')
d.click()
time.sleep(1)

driver.get('http://192.168.1.1/system_reboot.asp')
#print driver.page_source
d = driver.find_element_by_id('rebootBtn')
d.click()
dir(driver)
alert = driver.switch_to_alert()
alert.accept()
print "rebooted successfully"
driver.quit()
display.stop()

