from pyvirtualdisplay import Display
from selenium import webdriver
import time

display = Display(visible=0, size=(800, 600))
display.start()


driver  = webdriver.Chrome()
driver.get('http://10.50.0.100/connect/PortalMain')
time.sleep(1)
try:
	d = driver.find_element_by_id('UserCheck_Logoff_Button_span')
	d.click()
	time.sleep(2)
except Exception, e:
	driver.quit()
	display.stop()

print "logged out"