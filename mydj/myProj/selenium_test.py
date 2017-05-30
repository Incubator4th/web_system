import os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def initWork():
	chromeOptions = webdriver.ChromeOptions()
	chromeOptions.add_argument('no-default-browser-check')
	chromeOptions.add_experimental_option('prefs', {
		'credentials_enable_service': False,
		'profile': {
			'credentials_enable_service': False,
			'password_manager_enabled': False
		}
	})

	chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
	os.environ['webdriver.chrome.driver'] = chromedriver
	driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=chromeOptions)
	return driver


def handleLogin(driver,username = 'admin',password = 'admin'):

	loginurl = 'http://127.0.0.1:8000/index/login/'
	t_logurl = 'http://127.0.0.1:8000/t_index/t_login/'
	adminurl = 'http://127.0.0.1:8000/admin/'
	driver.set_window_size(800,600)
	driver.get(loginurl)
	sleep(5)
	driver.get(t_logurl)
	sleep(5)
	driver.get(adminurl)
	sleep(5)
	driver.get(loginurl)

	elem = driver.find_element_by_xpath("//*[@id='id_username']")
	elem.send_keys('学生')

	#elem.click()


if __name__ == '__main__':
	driver = initWork()
	handleLogin(driver)
	driver.close()
	driver.quit()
