from pyvirtualdisplay import Display
from selenium import webdriver
import time
from getpass import getpass
import sys
display = Display(visible=0, size=(800, 600))
display.start()


driver  = webdriver.Chrome()
driver.get('http://10.50.0.100/connect/PortalMain')
time.sleep(1)
try:
	d = driver.find_element_by_id('LoginUserPassword_auth_username')
except Exception, e:
	print "reboot the router"
	driver.quit()
	display.exit()
	sys.exit()

d.send_keys('bt2k15a2177')
d = driver.find_element_by_id('LoginUserPassword_auth_password')
pwd = getpass()
d.send_keys(pwd)
d = driver.find_element_by_id('UserCheck_Login_Button_span')
d.click()
time.sleep(2)
valid = True
try:
	d = driver.find_element_by_id('LoginUserPassword_error_message')
except Exception, e:
	valid = False

if valid:
	print "Error logging in"
else:
	print "logged in successfully"
driver.quit()
display.stop()
